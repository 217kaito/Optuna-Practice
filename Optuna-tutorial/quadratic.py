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

'''
実行結果

>>> import optuna
>>> 
>>> def objective(trial):
...     x = trial.suggest_float("x", -10, 10)
...     return (x - 2) ** 2
... 
>>> study = optuna.create_study()
[I 2024-08-28 06:21:34,386] A new study created in memory with name: no-name-2ef24b86-602d-4e4c-a8f2-150852c93fbd
>>> study.optimize(objective, n_trials=100)
[I 2024-08-28 06:21:34,391] Trial 0 finished with value: 104.41366421627134 and parameters: {'x': -8.218300456351406}. Best is trial 0 with value: 104.41366421627134.
[I 2024-08-28 06:21:34,392] Trial 1 finished with value: 27.186569073086396 and parameters: {'x': -3.2140741338310868}. Best is trial 1 with value: 27.186569073086396.
params
found_x = best_params["x"]
print("Found x: [I 2024-08-28 06:21:34,393] Trial 2 finished with value: 104.04312350865877 and parameters: {'x': -8.200153112020367}. Best is trial 1 with value: 27.186569073086396.
[I 2024-08-28 06:21:34,397] Trial 3 finished with value: 57.33282127494964 and parameters: {'x': -5.571843981154765}. Best is trial 1 with value: 27.186569073086396.
[I 2024-08-28 06:21:34,397] Trial 4 finished with value: 63.06098774604792 and parameters: {'x': -5.941094870737153}. Best is trial 1 with value: 27.186569073086396.
[I 2024-08-28 06:21:34,398] Trial 5 finished with value: 65.5096996141259 and parameters: {'x': -6.093806250098028}. Best is trial 1 with value: 27.186569073086396.
[I 2024-08-28 06:21:34,398] Trial 6 finished with value: 59.10374693884303 and parameters: {'x': 9.687896132157551}. Best is trial 1 with value: 27.186569073086396.
[I 2024-08-28 06:21:34,399] Trial 7 finished with value: 0.17296690675310006 and parameters: {'x': 2.415892902984771}. Best is trial 7 with value: 0.17296690675310006.
{}, (x - 2)^2: {}".format(found_x, (found_x - 2) *[I 2024-08-28 06:21:34,399] Trial 8 finished with value: 102.79487705710308 and parameters: {'x': -8.138780846684826}. Best is trial 7 with value: 0.17296690675310006.
[I 2024-08-28 06:21:34,400] Trial 9 finished with value: 19.314962490926415 and parameters: {'x': 6.394879121309984}. Best is trial 7 with value: 0.17296690675310006.
* 2))
[I 2024-08-28 06:21:34,405] Trial 10 finished with value: 0.020207712513295208 and parameters: {'x': 2.142153833973253}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,409] Trial 11 finished with value: 0.031267580561169066 and parameters: {'x': 2.1768264136410878}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,412] Trial 12 finished with value: 0.4976495887515916 and parameters: {'x': 1.2945571683321238}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,415] Trial 13 finished with value: 5.349896699444748 and parameters: {'x': 4.312984370773989}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,418] Trial 14 finished with value: 13.358762441838962 and parameters: {'x': -1.6549640821544283}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,421] Trial 15 finished with value: 8.958830545898449 and parameters: {'x': 4.993130559447491}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,425] Trial 16 finished with value: 7.702809026764137 and parameters: {'x': -0.775393490437732}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,428] Trial 17 finished with value: 48.57785312320765 and parameters: {'x': 8.969781425784287}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,431] Trial 18 finished with value: 0.16436571735537106 and parameters: {'x': 2.4054204204962684}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,434] Trial 19 finished with value: 25.88659809430593 and parameters: {'x': 7.087887390096791}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,437] Trial 20 finished with value: 21.893240562545767 and parameters: {'x': -2.6790213252929043}. Best is trial 10 with value: 0.020207712513295208.
[I 2024-08-28 06:21:34,440] Trial 21 finished with value: 0.0009328308027892815 and parameters: {'x': 2.030542278939026}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,444] Trial 22 finished with value: 1.1577279672032978 and parameters: {'x': 3.0759776796956793}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,447] Trial 23 finished with value: 1.8959481758178116 and parameters: {'x': 0.6230656603099001}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,450] Trial 24 finished with value: 6.689626372196189 and parameters: {'x': 4.5864312038397985}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,453] Trial 25 finished with value: 2.8765588200935284 and parameters: {'x': 0.3039578955422336}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,456] Trial 26 finished with value: 23.305310570453567 and parameters: {'x': 6.827557412445094}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,460] Trial 27 finished with value: 1.7188682555205164 and parameters: {'x': 3.3110561603228583}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,463] Trial 28 finished with value: 0.27362440424839474 and parameters: {'x': 1.4769087993013124}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,466] Trial 29 finished with value: 5.205118367719716 and parameters: {'x': -0.281472850533119}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,469] Trial 30 finished with value: 13.579964058281366 and parameters: {'x': 5.685100277913936}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,473] Trial 31 finished with value: 0.022914741886963172 and parameters: {'x': 1.848623839766748}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,476] Trial 32 finished with value: 13.88215504321039 and parameters: {'x': -1.7258764127665844}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,479] Trial 33 finished with value: 3.0987313922361563 and parameters: {'x': 3.7603213889049227}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,482] Trial 34 finished with value: 0.7689893151073116 and parameters: {'x': 1.1230796415253483}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,486] Trial 35 finished with value: 34.42815889115479 and parameters: {'x': -3.8675513539426984}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,490] Trial 36 finished with value: 0.004376176958769585 and parameters: {'x': 1.9338473208496467}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,493] Trial 37 finished with value: 11.210059090980346 and parameters: {'x': -1.348142633010181}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,496] Trial 38 finished with value: 42.484192325842095 and parameters: {'x': -4.51798989918227}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,500] Trial 39 finished with value: 38.85573910656603 and parameters: {'x': 8.233437182371057}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,503] Trial 40 finished with value: 0.0025773280860709583 and parameters: {'x': 2.0507673919565597}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,506] Trial 41 finished with value: 0.1138992398684631 and parameters: {'x': 2.3374896144601536}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,509] Trial 42 finished with value: 4.065179358606329 and parameters: {'x': -0.01622899458526983}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,513] Trial 43 finished with value: 0.2242015530064677 and parameters: {'x': 1.52650073600219}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,516] Trial 44 finished with value: 2.1785765284595766 and parameters: {'x': 3.476000179017461}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,520] Trial 45 finished with value: 11.154023378861648 and parameters: {'x': 5.339763970531697}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,523] Trial 46 finished with value: 4.242852091190223 and parameters: {'x': 4.05981846073634}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,526] Trial 47 finished with value: 0.00471598923597746 and parameters: {'x': 1.9313269395179051}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,530] Trial 48 finished with value: 0.5339031096454451 and parameters: {'x': 2.7306867383807134}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,533] Trial 49 finished with value: 0.9443516451667391 and parameters: {'x': 1.0282224301998224}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,536] Trial 50 finished with value: 122.53054137111104 and parameters: {'x': -9.069351443111337}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,539] Trial 51 finished with value: 0.004294465681169177 and parameters: {'x': 2.065532172870806}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,543] Trial 52 finished with value: 6.986072119906091 and parameters: {'x': -0.6431178785491372}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,546] Trial 53 finished with value: 0.02569124792352193 and parameters: {'x': 2.1602848961178873}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,549] Trial 54 finished with value: 2.073254925307262 and parameters: {'x': 0.5601198225868718}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,553] Trial 55 finished with value: 1.2425841650838243 and parameters: {'x': 3.114712593040836}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,556] Trial 56 finished with value: 18.127526209561015 and parameters: {'x': -2.2576432694110267}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,560] Trial 57 finished with value: 6.162289262764864 and parameters: {'x': 4.482395871484817}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,563] Trial 58 finished with value: 16.461058886341146 and parameters: {'x': 6.057223051095558}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,566] Trial 59 finished with value: 1.7941300321929814 and parameters: {'x': 0.6605486077527929}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,570] Trial 60 finished with value: 9.367733559192615 and parameters: {'x': -1.0606753436443754}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,573] Trial 61 finished with value: 0.02668980415375492 and parameters: {'x': 2.1633701446218216}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,576] Trial 62 finished with value: 0.156259309409909 and parameters: {'x': 1.6047035170787514}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,580] Trial 63 finished with value: 0.06627187431555756 and parameters: {'x': 1.7425667575553663}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,583] Trial 64 finished with value: 0.8226745995940409 and parameters: {'x': 2.9070141121250765}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,587] Trial 65 finished with value: 4.998466771501261 and parameters: {'x': -0.23572511089831005}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,590] Trial 66 finished with value: 2.5845027468555846 and parameters: {'x': 3.607638873272099}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,593] Trial 67 finished with value: 6.625958334465479 and parameters: {'x': 4.574093691858453}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,597] Trial 68 finished with value: 1.146916358669034 and parameters: {'x': 0.9290581908109881}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,600] Trial 69 finished with value: 0.2091530473457358 and parameters: {'x': 2.4573325347553308}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,604] Trial 70 finished with value: 3.5300496677959434 and parameters: {'x': 3.878842640509296}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,607] Trial 71 finished with value: 0.13039571203693173 and parameters: {'x': 1.6388965355511917}. Best is trial 21 with value: 0.0009328308027892815.
[I 2024-08-28 06:21:34,611] Trial 72 finished with value: 0.0005685930772588153 and parameters: {'x': 2.023845189813856}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,614] Trial 73 finished with value: 3.1621602505508797 and parameters: {'x': 0.22175360240745046}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,618] Trial 74 finished with value: 0.004821703820168618 and parameters: {'x': 2.069438489472112}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,621] Trial 75 finished with value: 1.3827768197549926 and parameters: {'x': 3.1759153114722984}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,624] Trial 76 finished with value: 0.244133568983321 and parameters: {'x': 2.4940987441628657}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,628] Trial 77 finished with value: 0.5619239696812447 and parameters: {'x': 1.2503841185772244}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,631] Trial 78 finished with value: 11.109277716038859 and parameters: {'x': 5.3330583127270454}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,635] Trial 79 finished with value: 0.003970256990991198 and parameters: {'x': 1.9369900246707619}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,638] Trial 80 finished with value: 6.813737381535336 and parameters: {'x': -0.6103136557768946}. Best is trial 72 with value: 0.0005685930772588153.
[I 2024-08-28 06:21:34,642] Trial 81 finished with value: 0.0002026364573408635 and parameters: {'x': 1.9857649567144717}. Best is trial 81 with value: 0.0002026364573408635.
[I 2024-08-28 06:21:34,645] Trial 82 finished with value: 0.5656066578319943 and parameters: {'x': 2.752068253439802}. Best is trial 81 with value: 0.0002026364573408635.
[I 2024-08-28 06:21:34,648] Trial 83 finished with value: 2.798500924042757 and parameters: {'x': 0.32712794152010627}. Best is trial 81 with value: 0.0002026364573408635.
[I 2024-08-28 06:21:34,652] Trial 84 finished with value: 5.145970901687209e-05 and parameters: {'x': 1.9928264577078774}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,655] Trial 85 finished with value: 0.7108408024126077 and parameters: {'x': 1.1568862458644102}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,659] Trial 86 finished with value: 2.3882029415070307 and parameters: {'x': 3.545381163825621}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,662] Trial 87 finished with value: 4.827493125547192 and parameters: {'x': 4.197155689874341}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,666] Trial 88 finished with value: 1.6418191627829577 and parameters: {'x': 0.718665085630241}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,669] Trial 89 finished with value: 0.5727611719594388 and parameters: {'x': 2.756809865130892}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,673] Trial 90 finished with value: 0.0010065588262726309 and parameters: {'x': 1.9682736887383259}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,676] Trial 91 finished with value: 0.0315460176585266 and parameters: {'x': 1.8223880137532193}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,680] Trial 92 finished with value: 0.437334087463904 and parameters: {'x': 1.338687602215183}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,683] Trial 93 finished with value: 1.4387501798833695 and parameters: {'x': 3.1994791285734694}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,687] Trial 94 finished with value: 0.0009119137297407114 and parameters: {'x': 2.0301979093604294}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,690] Trial 95 finished with value: 0.1485659160570119 and parameters: {'x': 2.385442493839239}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,694] Trial 96 finished with value: 79.2507706138547 and parameters: {'x': -6.90229018926336}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,697] Trial 97 finished with value: 3.204288273597451 and parameters: {'x': 0.20994741038218345}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,701] Trial 98 finished with value: 8.928419474030443 and parameters: {'x': 4.98804609636974}. Best is trial 84 with value: 5.145970901687209e-05.
[I 2024-08-28 06:21:34,704] Trial 99 finished with value: 1.1582023257401117 and parameters: {'x': 0.9238019114772078}. Best is trial 84 with value: 5.145970901687209e-05.
>>> 
>>> best_params = study.best_params
>>> found_x = best_params["x"]
>>> print("Found x: {}, (x - 2)^2: {}".format(found_x, (found_x - 2) ** 2))
Found x: 1.9928264577078774, (x - 2)^2: 5.145970901687209e-05
>>> 

'''