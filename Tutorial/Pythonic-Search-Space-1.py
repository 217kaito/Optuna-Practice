import optuna


def objective(trial):
    # Categorical parameter
    # 最適化アルゴリズムとして、"MomentumSGD" または "Adam" を選択する。
    optimizer = trial.suggest_categorical("optimizer", ["MomentumSGD", "Adam"])

    # Integer parameter
    # ニューラルネットワークの層の数として、1から3までの整数から提案する。
    num_layers = trial.suggest_int("num_layers", 1, 3)

    # Integer parameter (log)
    # 各層のチャネル数(フィルタ数)を32から512の範囲で、対数スケールに基づいて提案する。
    num_channels = trial.suggest_int("num_channels", 32, 512, log=True)

    # Integer parameter (discretized)
    # 各層のユニット数(ノード数)を10から100までの範囲で、5単位のステップで提案する。つまり、10,15,20,...100のいずれかが選ばれる。
    num_units = trial.suggest_int("num_units", 10, 100, step=5)

    # Floating point parameter
    # ドロップアウト率を0.0から1.0までの範囲で提案する。
    dropout_rate = trial.suggest_float("dropout_rate", 0.0, 1.0)

    # Floating point parameter (log)
    # 学習率を1e-5から1e-2までの範囲で、対数スケールに基づいて提案する。
    learning_rate = trial.suggest_float("learning_rate", 1e-5, 1e-2, log=True)

    # Floating point parameter (discretized)
    # "drop_path_rate" を0.0から1.0までの範囲で、0.1単位で提案する。つまり、0.0, 0.1, 0.2, ... 1.0 のいずれかが選ばれる。
    drop_path_rate = trial.suggest_float("drop_path_rate", 0.0, 1.0, step=0.1)