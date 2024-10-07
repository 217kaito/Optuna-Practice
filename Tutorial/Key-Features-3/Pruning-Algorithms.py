# Optunaにおいて、Prunerはトレーニングの初期段階で見込みのないTrialを自動的に停止します。
# Optunaでは、いくつかのPrunerアルゴリズムが提供されています。

# 剪定機能を有効にするには、反復トレーニングの各ステップの後に、report()と、should_prune()を呼び出す必要があります。
# report()は、中間目標値を定期的に監視します。should_prune()は、事前に定義された条件を満たさないtrialの終了を決定します。

# 機械学習フレームには統合モジュールを使用することが推奨されます。

import optuna
import logging
import sys
import sklearn.datasets
import sklearn.linear_model
import sklearn.model_selection

def objective(trial):
    iris = sklearn.datasets.load_iris()
    classes = list(set(iris.target))
    train_x, valid_x, train_y, valid_y = sklearn.model_selection.train_test_split(
        iris.data, iris.target, test_size=0.25, random_state=0
    )

    alpha = trial.suggest_float("alpha", 1e-5, 1e-1, log=True)
    clf = sklearn.linear_model.SGDClassifier(alpha=alpha)

    for step in range(100):
        clf.partial_fit(train_x, train_y, classes=classes)

        # Report intermediate objective value.
        intermediate_value = 1.0 - clf.score(valid_x, valid_y)
        trial.report(intermediate_value, step)

        # Handle pruning based on the intermediate value.
        if trial.should_prune():
            raise optuna.TrialPruned()

    return 1.0 - clf.score(valid_x, valid_y)


# 剪定条件として中央値停止ルールを設定します。
# 各trialの途中結果をもとに、その試行のパフォーマンスがこれまでに行ったほかの試行の中央値よりも悪い場合、
# 早期にその思考を停止するという仕組みです。

# Add stream handler of stdout to show the messages
optuna.logging.get_logger("optuna").addHandler(logging.StreamHandler(sys.stdout))
study = optuna.create_study(pruner=optuna.pruners.MedianPruner())
study.optimize(objective, n_trials=20)

'''
[I 2024-10-07 08:12:26,037] A new study created in memory with name: no-name-ca8c273d-9bf0-4ee5-99cd-d45bc3391174
A new study created in memory with name: no-name-ca8c273d-9bf0-4ee5-99cd-d45bc3391174
[I 2024-10-07 08:12:26,192] Trial 0 finished with value: 0.26315789473684215 and parameters: {'alpha': 0.004166030467920785}. Best is trial 0 with value: 0.26315789473684215.
Trial 0 finished with value: 0.26315789473684215 and parameters: {'alpha': 0.004166030467920785}. Best is trial 0 with value: 0.26315789473684215.
[I 2024-10-07 08:12:26,345] Trial 1 finished with value: 0.07894736842105265 and parameters: {'alpha': 0.00024370288640338834}. Best is trial 1 with value: 0.07894736842105265.
Trial 1 finished with value: 0.07894736842105265 and parameters: {'alpha': 0.00024370288640338834}. Best is trial 1 with value: 0.07894736842105265.
[I 2024-10-07 08:12:26,497] Trial 2 finished with value: 0.1578947368421053 and parameters: {'alpha': 0.0005207469697356998}. Best is trial 1 with value: 0.07894736842105265.
Trial 2 finished with value: 0.1578947368421053 and parameters: {'alpha': 0.0005207469697356998}. Best is trial 1 with value: 0.07894736842105265.
[I 2024-10-07 08:12:26,648] Trial 3 finished with value: 0.02631578947368418 and parameters: {'alpha': 0.0014383096710774651}. Best is trial 3 with value: 0.02631578947368418.
Trial 3 finished with value: 0.02631578947368418 and parameters: {'alpha': 0.0014383096710774651}. Best is trial 3 with value: 0.02631578947368418.
[I 2024-10-07 08:12:26,800] Trial 4 finished with value: 0.26315789473684215 and parameters: {'alpha': 0.0037995528547380814}. Best is trial 3 with value: 0.02631578947368418.
Trial 4 finished with value: 0.26315789473684215 and parameters: {'alpha': 0.0037995528547380814}. Best is trial 3 with value: 0.02631578947368418.
[I 2024-10-07 08:12:26,810] Trial 5 pruned. 
Trial 5 pruned. 
[I 2024-10-07 08:12:26,819] Trial 6 pruned. 
Trial 6 pruned. 
[I 2024-10-07 08:12:26,829] Trial 7 pruned. 
Trial 7 pruned. 
[I 2024-10-07 08:12:26,839] Trial 8 pruned. 
Trial 8 pruned. 
[I 2024-10-07 08:12:26,855] Trial 9 pruned. 
Trial 9 pruned. 
[I 2024-10-07 08:12:26,874] Trial 10 pruned. 
Trial 10 pruned. 
[I 2024-10-07 08:12:26,894] Trial 11 pruned. 
Trial 11 pruned. 
[I 2024-10-07 08:12:26,926] Trial 12 pruned. 
Trial 12 pruned. 
[I 2024-10-07 08:12:26,942] Trial 13 pruned. 
Trial 13 pruned. 
[I 2024-10-07 08:12:26,954] Trial 14 pruned. 
Trial 14 pruned. 
[I 2024-10-07 08:12:26,960] Trial 15 pruned. 
Trial 15 pruned. 
[I 2024-10-07 08:12:27,131] Trial 16 finished with value: 0.13157894736842102 and parameters: {'alpha': 0.0014063562959847774}. Best is trial 3 with value: 0.02631578947368418.
Trial 16 finished with value: 0.13157894736842102 and parameters: {'alpha': 0.0014063562959847774}. Best is trial 3 with value: 0.02631578947368418.
[I 2024-10-07 08:12:27,300] Trial 17 finished with value: 0.26315789473684215 and parameters: {'alpha': 0.04129232588889358}. Best is trial 3 with value: 0.02631578947368418.
Trial 17 finished with value: 0.26315789473684215 and parameters: {'alpha': 0.04129232588889358}. Best is trial 3 with value: 0.02631578947368418.
[I 2024-10-07 08:12:27,306] Trial 18 pruned. 
Trial 18 pruned. 
[I 2024-10-07 08:12:27,313] Trial 19 pruned. 
Trial 19 pruned.
'''