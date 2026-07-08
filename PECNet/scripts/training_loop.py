import argparse
import sys
import time

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import yaml

sys.path.append("../utils/")
from models import *
from social_utils import *

# hyper_params["optimizer"] の値に対応するオプティマイザの生成方法
OPTIMIZER_BUILDERS = {
    "Adam": lambda params, lr: optim.Adam(params, lr=lr),
    "SGD": lambda params, lr: optim.SGD(params, lr=lr),
    "Momentum": lambda params, lr: optim.SGD(params, lr=lr, momentum=0.9),
    "NAG": lambda params, lr: optim.SGD(params, lr=lr, momentum=0.9, nesterov=True),
    "Adagrad": lambda params, lr: optim.Adagrad(params, lr=lr),
    "RMSprop": lambda params, lr: optim.RMSprop(params, lr=lr),
    "AdamW": lambda params, lr: optim.AdamW(params, lr=lr),
    "AdaMax": lambda params, lr: optim.Adamax(params, lr=lr),
    "Nadam": lambda params, lr: optim.NAdam(params, lr=lr),
}


def parse_args():
    parser = argparse.ArgumentParser(description='PECNet')
    parser.add_argument('--num_workers', '-nw', type=int, default=0)
    parser.add_argument('--gpu_index', '-gi', type=int, default=0)
    parser.add_argument('--config_filename', '-cfn', type=str, default='optimal.yaml')
    parser.add_argument('--save_file', '-sf', type=str, default='PECNET_social_model.pt')
    parser.add_argument('--verbose', '-v', action='store_true')
    return parser.parse_args()


def setup_device(gpu_index):
    device = torch.device('cuda', index=gpu_index) if torch.cuda.is_available() else torch.device('cpu')
    if torch.cuda.is_available():
        torch.cuda.set_device(gpu_index)
    return device


def load_hyper_params(config_filename):
    with open("../config/" + config_filename, 'r') as file:
        hyper_params = yaml.load(file, Loader=yaml.FullLoader)
    return fill_default_hyper_params(hyper_params)


def build_optimizer(model, hyper_params):
    name = hyper_params.get("optimizer", "Adam")
    if name not in OPTIMIZER_BUILDERS:
        raise ValueError(f"Unsupported optimizer type: {name}")
    return OPTIMIZER_BUILDERS[name](model.parameters(), hyper_params["learning_rate"])


def load_datasets(hyper_params, verbose):
    train_dataset = SocialDataset(set_name="train", b_size=hyper_params["train_b_size"], t_tresh=hyper_params["time_thresh"], d_tresh=hyper_params["dist_thresh"], verbose=verbose)
    test_dataset = SocialDataset(set_name="test", b_size=hyper_params["test_b_size"], t_tresh=hyper_params["time_thresh"], d_tresh=hyper_params["dist_thresh"], verbose=verbose)

    # shift origin and scale data
    for dataset in (train_dataset, test_dataset):
        for traj in dataset.trajectory_batches:
            traj -= traj[:, :1, :]
            traj *= hyper_params["data_scale"]

    return train_dataset, test_dataset


def save_model_with_retry(save_path, hyper_params, model, optimizer, max_retries=10, wait_time=10):
    for attempt in range(max_retries):
        try:
            torch.save({
                'hyper_params': hyper_params,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict()
            }, save_path)
            print("モデルが正常に保存されました。")
            break
        except RuntimeError as e:
            print(f"モデルの保存に失敗しました。リトライします... ({attempt + 1}/{max_retries})")
            print(f"エラー: {e}")
            time.sleep(wait_time)
    else:
        print("モデルの保存に失敗しました。最大リトライ回数に達しました。")


def train(model, optimizer, train_dataset, hyper_params, device):

    model.train()
    train_loss = 0
    total_rcl, total_kld, total_adl = 0, 0, 0
    criterion = nn.MSELoss()

    for i, (traj, mask, initial_pos) in enumerate(zip(train_dataset.trajectory_batches, train_dataset.mask_batches, train_dataset.initial_pos_batches)):
        traj, mask, initial_pos = torch.DoubleTensor(traj).to(device), torch.DoubleTensor(mask).to(device), torch.DoubleTensor(initial_pos).to(device)
        x = traj[:, :hyper_params['past_length'], :]
        y = traj[:, hyper_params['past_length']:, :]

        x = x.contiguous().view(-1, x.shape[1]*x.shape[2]) # (x,y,x,y ... )
        x = x.to(device)
        dest = y[:, -1, :].to(device)
        future = y[:, :-1, :].contiguous().view(y.size(0),-1).to(device)

        dest_recon, mu, var, interpolated_future = model.forward(x, initial_pos, dest=dest, mask=mask, device=device)

        optimizer.zero_grad()
        rcl, kld, adl = calculate_loss(dest, dest_recon, mu, var, criterion, future, interpolated_future)
        loss = rcl + kld*hyper_params["kld_reg"] + adl*hyper_params["adl_reg"]
        loss.backward()

        train_loss += loss.item()
        total_rcl += rcl.item()
        total_kld += kld.item()
        total_adl += adl.item()
        optimizer.step()

    return train_loss, total_rcl, total_kld, total_adl


def test(model, test_dataset, hyper_params, device, best_of_n=1):
    '''Evalutes test metrics. Assumes all test data is in one batch'''

    model.eval()
    assert best_of_n >= 1 and type(best_of_n) == int

    with torch.no_grad():
        for i, (traj, mask, initial_pos) in enumerate(zip(test_dataset.trajectory_batches, test_dataset.mask_batches, test_dataset.initial_pos_batches)):
            traj, mask, initial_pos = torch.DoubleTensor(traj).to(device), torch.DoubleTensor(mask).to(device), torch.DoubleTensor(initial_pos).to(device)
            x = traj[:, :hyper_params['past_length'], :]
            y = traj[:, hyper_params['past_length']:, :]
            y = y.cpu().numpy()

            # reshape the data
            x = x.view(-1, x.shape[1]*x.shape[2])
            x = x.to(device)

            dest = y[:, -1, :]
            all_l2_errors_dest = []
            all_guesses = []
            for _ in range(best_of_n):

                dest_recon = model.forward(x, initial_pos, device=device)
                dest_recon = dest_recon.cpu().numpy()
                all_guesses.append(dest_recon)

                l2error_sample = np.linalg.norm(dest_recon - dest, axis = 1)
                all_l2_errors_dest.append(l2error_sample)

            all_l2_errors_dest = np.array(all_l2_errors_dest)
            all_guesses = np.array(all_guesses)
            # average error
            l2error_avg_dest = np.mean(all_l2_errors_dest)

            # choosing the best guess
            indices = np.argmin(all_l2_errors_dest, axis = 0)

            best_guess_dest = all_guesses[indices,np.arange(x.shape[0]),  :]

            # taking the minimum error out of all guess
            l2error_dest = np.mean(np.min(all_l2_errors_dest, axis = 0))

            best_guess_dest = torch.DoubleTensor(best_guess_dest).to(device)

            # using the best guess for interpolation
            interpolated_future = model.predict(x, best_guess_dest, mask, initial_pos)
            interpolated_future = interpolated_future.cpu().numpy()
            best_guess_dest = best_guess_dest.cpu().numpy()

            # final overall prediction
            predicted_future = np.concatenate((interpolated_future, best_guess_dest), axis = 1)
            predicted_future = np.reshape(predicted_future, (-1, hyper_params['future_length'], 2)) # making sure
            # ADE error
            l2error_overall = np.mean(np.linalg.norm(y - predicted_future, axis = 2))

            l2error_overall /= hyper_params["data_scale"]
            l2error_dest /= hyper_params["data_scale"]
            l2error_avg_dest /= hyper_params["data_scale"]

            print('Test time error in destination best: {:0.3f} and mean: {:0.3f}'.format(l2error_dest, l2error_avg_dest))
            print('Test time error overall (ADE) best: {:0.3f}'.format(l2error_overall))

    return l2error_overall, l2error_dest, l2error_avg_dest


def main():
    args = parse_args()

    torch.set_default_dtype(torch.float64)
    device = setup_device(args.gpu_index)
    print(device)

    hyper_params = load_hyper_params(args.config_filename)
    print(f"hyper_params: {hyper_params}")

    model = pecnet_from_hyper_params(hyper_params, args.verbose)
    model = model.double().to(device)

    optimizer = build_optimizer(model, hyper_params)
    print(f"optimizer: {optimizer}")

    train_dataset, test_dataset = load_datasets(hyper_params, args.verbose)

    best_test_loss = float('inf') # start saving after this threshold
    best_endpoint_loss = 50
    N = hyper_params["n_values"]

    for e in range(hyper_params['num_epochs']):
        train_loss, rcl, kld, adl = train(model, optimizer, train_dataset, hyper_params, device)
        test_loss, final_point_loss_best, final_point_loss_avg = test(model, test_dataset, hyper_params, device, best_of_n=N)

        if best_test_loss > test_loss:
            print("Epoch: ", e)
            print('################## BEST PERFORMANCE {:0.2f} ########'.format(test_loss))
            best_test_loss = test_loss
            save_path = '../saved_models/' + args.save_file
            save_model_with_retry(save_path, hyper_params, model, optimizer)
            print("Saved model to:\n{}".format(save_path))

        if final_point_loss_best < best_endpoint_loss:
            best_endpoint_loss = final_point_loss_best

        print("Train Loss", train_loss)
        print("RCL", rcl)
        print("KLD", kld)
        print("ADL", adl)
        print("Test ADE", test_loss)
        print("Test Average FDE (Across  all samples)", final_point_loss_avg)
        print("Test Min FDE", final_point_loss_best)
        print("Test Best ADE Loss So Far (N = {})".format(N), best_test_loss)
        print("Test Best Min FDE (N = {})".format(N), best_endpoint_loss)


if __name__ == "__main__":
    main()
