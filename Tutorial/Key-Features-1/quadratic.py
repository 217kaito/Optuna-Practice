import optuna

# 目的関数を定義
def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x - 2) ** 2

# Studyの作成
study = optuna.create_study()
# 最適化の開始
study.optimize(objective, n_trials=100)

# 結果を出力
best_params = study.best_params
found_x = best_params["x"]
print("Found x: {}, (x - 2)^2: {}".format(found_x, (found_x - 2) ** 2))
# この方法でもいい
print("Found x: {}, (x - 2)^2: {}".format(study.best_params, study.best_value))

# 最良のトライアルを得る(最良のトライアルのFrozenTrialオブジェクトという詳細な結果が出力される。)
study.best_trial

# すべてのトライアルを得る
study.trials
# 1,2番目のトライアルを得る
for trial in study.trials[:2]:
    print(trial)

# トライアルの数を得る
len(study.trials)

# 再度optimizeを実行することによって、最適化を継続できる
study.optimize(objective, n_trials=100)

# trialの数は200となる
len(study.trials)

# 今回の目的関数は非常に簡単なため、結果は改善されないが、より複雑なものだと改善が見込める
best_params = study.best_params
found_x = best_params["x"]
print("Found x: {}, (x - 2)^2: {}".format(found_x, (found_x - 2) ** 2))


'''
実行結果（抜粋）

>>> # Studyの作成
>>> study = optuna.create_study()
[I 2024-08-28 09:53:29,661] A new study created in memory with name: no-name-85bcf2d0-0151-4af7-9cf8-ec11899d5648
>>> # 最適化の開始
>>> study.optimize(objective, n_trials=100)
[I 2024-08-28 09:53:29,667] Trial 0 finished with value: 3.568127778787722 and parameters: {'x': 3.888948855524607}. Best is trial 0 with value: 3.568127778787722.
[I 2024-08-28 09:53:29,668] Trial 1 finished with value: 5.710452974503992 and parameters: {'x': 4.389655409155051}. Best is trial 0 with value: 3.568127778787722.
（中略: Trial 2〜98）
[I 2024-08-28 09:53:29,975] Trial 99 finished with value: 3.0123555445489214 and parameters: {'x': 0.2643861188187848}. Best is trial 74 with value: 0.00017668117080590743.
>>>
>>> # 結果を出力
>>> best_params = study.best_params
>>> found_x = best_params["x"]
>>> print("Found x: {}, (x - 2)^2: {}".format(found_x, (found_x - 2) ** 2))
Found x: 1.9867078530400124, (x - 2)^2: 0.00017668117080590743
>>> # この方法でもいい
>>> print("Found x: {}, (x - 2)^2: {}".format(study.best_params, study.best_value))
Found x: {'x': 1.9867078530400124}, (x - 2)^2: 0.00017668117080590743
>>>
>>> # 最良のトライアルを得る(最良のトライアルのFrozenTrialオブジェクトという詳細な結果が出力される。)
>>> study.best_trial
FrozenTrial(number=74, state=TrialState.COMPLETE, values=[0.00017668117080590743], datetime_start=datetime.datetime(2024, 8, 28, 9, 53, 29, 886753), datetime_complete=datetime.datetime(2024, 8, 28, 9, 53, 29, 889944), params={'x': 1.9867078530400124}, user_attrs={}, system_attrs={}, intermediate_values={}, distributions={'x': FloatDistribution(high=10.0, log=False, low=-10.0, step=None)}, trial_id=74, value=None)
>>>
>>> # 1,2番目のトライアルを得る
>>> for trial in study.trials[:2]:
...     print(trial)
...
FrozenTrial(number=0, state=TrialState.COMPLETE, values=[3.568127778787722], ..., params={'x': 3.888948855524607}, ..., trial_id=0, value=None)
FrozenTrial(number=1, state=TrialState.COMPLETE, values=[5.710452974503992], ..., params={'x': 4.389655409155051}, ..., trial_id=1, value=None)
>>> # トライアルの数を得る
>>> len(study.trials)
100
>>>
>>> # 再度optimizeを実行することによって、最適化を継続できる
>>> study.optimize(objective, n_trials=100)
[I 2024-08-28 09:53:29,994] Trial 100 finished with value: 0.3665789233492631 and parameters: {'x': 2.60545761482474}. Best is trial 74 with value: 0.00017668117080590743.
（中略: Trial 101〜198）
[I 2024-08-28 09:53:30,357] Trial 199 finished with value: 0.19578534873508632 and parameters: {'x': 1.5575236178787772}. Best is trial 196 with value: 3.540331112750418e-05.
>>>
>>> # trialの数は200となる
>>> len(study.trials)
200
>>>
>>> # 今回の目的関数は非常に簡単なため、結果は改善されないが、より複雑なものだと改善が見込める
>>> best_params = study.best_params
>>> found_x = best_params["x"]
>>> print("Found x: {}, (x - 2)^2: {}".format(found_x, (found_x - 2) ** 2))
Found x: 2.0059500681615847, (x - 2)^2: 3.540331112750418e-05
'''
