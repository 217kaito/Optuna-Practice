# Optunaはサンプラーを用いて最適なパラメータを導きます。
# デフォルトのサンプラーはTRESamplerですが、いくつかのサンプリングアルゴリズムが提供されています。
import optuna

# TRESamplerは以下のように使用します。
study = optuna.create_study()
print(f"Sampler is {study.sampler.__class__.__name__}")

# 異なるサンプラーを使用したい場合(今回はRandomSamplerやCmaEsSampler)
study = optuna.create_study(sampler=optuna.samplers.RandomSampler())
print(f"Sampler is {study.sampler.__class__.__name__}")

study = optuna.create_study(sampler=optuna.samplers.CmaEsSampler())
print(f"Sampler is {study.sampler.__class__.__name__}")

'''
>>> import optuna
>>> 
>>> # TRESamplerは以下のように使用します。
>>> study = optuna.create_study()
[I 2024-09-23 08:55:56,437] A new study created in memory with name: no-name-6f2d2316-1d77-47d1-a98b-1bb2fd6e6e21
>>> print(f"Sampler is {study.sampler.__class__.__name__}")
Sampler is TPESampler
>>> 
>>> # 異なるサンプラーを使用したい場合(今回はRandomSamplerやCmaEsSampler)
>>> study = optuna.create_study(sampler=optuna.samplers.RandomSampler())
[I 2024-09-23 08:55:56,451] A new study created in memory with name: no-name-21e8d5f0-5b71-45b4-8841-7107d85ee621
>>> print(f"Sampler is {study.sampler.__class__.__name__}")
Sampler is RandomSampler
>>> 
>>> study = optuna.create_study(sampler=optuna.samplers.CmaEsSampler())
[I 2024-09-23 08:55:56,466] A new study created in memory with name: no-name-58879254-d7d1-4032-9ee7-de65e89e4db3
>>> print(f"Sampler is {study.sampler.__class__.__name__}")
Sampler is CmaEsSampler
'''