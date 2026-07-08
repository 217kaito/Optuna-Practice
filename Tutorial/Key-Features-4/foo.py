import optuna


def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x - 2) ** 2


if __name__ == "__main__":
    # load_study関数を使用して、MySQLデータベースに保存された既存のstudyをロードする。
    study = optuna.load_study(
        # studyとstudyが保存されるデータベースに接続する。
        # ユーザーに対してパスワードを設定している場合はPassword部分にそれを入力する。設定していない場合は省略できる。
        # getpassモジュールを使って、実行時にパスワードを入力するようにするとよさそう。
        study_name="distributed-example", storage="mysql://root:Password@host-name/example"
    )
    study.optimize(objective, n_trials=100)

# 二つのプロセスで分散最適化を実行する
'''
Process1の実行結果（抜粋）
[I 2024-10-21 09:05:21,808] Trial 100 finished with value: 1.582748722300218 and parameters: {'x': 0.7419265831040631}. Best is trial 22 with value: 8.756547215959814e-05.
[I 2024-10-21 09:05:21,850] Trial 101 finished with value: 0.019915853495189605 and parameters: {'x': 1.8588764601663152}. Best is trial 22 with value: 8.756547215959814e-05.
[I 2024-10-21 09:05:21,886] Trial 102 finished with value: 2.1031661413949087e-06 and parameters: {'x': 2.0014502296857377}. Best is trial 102 with value: 2.1031661413949087e-06.
（中略）
[I 2024-10-21 09:05:23,398] Trial 152 finished with value: 8.967267105719848e-07 and parameters: {'x': 2.0009469565515756}. Best is trial 152 with value: 8.967267105719848e-07.
（中略）
[I 2024-10-21 09:05:26,010] Trial 281 finished with value: 0.02148428042327362 and parameters: {'x': 1.853424830127086}. Best is trial 152 with value: 8.967267105719848e-07.
'''

'''
Process2の実行結果（抜粋）
[I 2024-10-21 09:05:22,732] Trial 120 finished with value: 0.05434891194753381 and parameters: {'x': 2.2331285309599274}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,771] Trial 123 finished with value: 0.010467745551631668 and parameters: {'x': 1.8976879989853015}. Best is trial 102 with value: 2.1031661413949087e-06.
（中略）
両プロセスが同一のstudyを共有しているため、trial番号が交互に進み、Bestトライアルも共有される。
[I 2024-10-21 09:05:26,864] Trial 298 finished with value: 0.4661093863906172 and parameters: {'x': 2.6827220418227444}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,919] Trial 299 finished with value: 0.006325126362469784 and parameters: {'x': 1.9204693369669925}. Best is trial 152 with value: 8.967267105719848e-07.
'''
