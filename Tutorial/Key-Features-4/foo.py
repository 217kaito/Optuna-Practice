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
Process1の実行結果
[I 2024-10-21 09:05:21,808] Trial 100 finished with value: 1.582748722300218 and parameters: {'x': 0.7419265831040631}. Best is trial 22 with value: 8.756547215959814e-05.
[I 2024-10-21 09:05:21,850] Trial 101 finished with value: 0.019915853495189605 and parameters: {'x': 1.8588764601663152}. Best is trial 22 with value: 8.756547215959814e-05.
[I 2024-10-21 09:05:21,886] Trial 102 finished with value: 2.1031661413949087e-06 and parameters: {'x': 2.0014502296857377}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:21,923] Trial 103 finished with value: 0.379652308841061 and parameters: {'x': 1.3838406790114581}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:21,968] Trial 104 finished with value: 0.08929946212961458 and parameters: {'x': 2.2988301559910154}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,006] Trial 105 finished with value: 0.9503483294628452 and parameters: {'x': 2.9748581073483695}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,044] Trial 106 finished with value: 0.012092673640626874 and parameters: {'x': 2.1099666933240555}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,081] Trial 107 finished with value: 0.3786748694388433 and parameters: {'x': 1.3846343611812215}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,119] Trial 108 finished with value: 2.6033354213482482 and parameters: {'x': 3.613485488421959}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,158] Trial 109 finished with value: 2.9185528760341723 and parameters: {'x': 0.29162273603452205}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,200] Trial 110 finished with value: 1.737497895024705 and parameters: {'x': 0.681858165816476}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,256] Trial 111 finished with value: 0.01902687703057377 and parameters: {'x': 1.8620620536959689}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,308] Trial 112 finished with value: 0.000564717905244093 and parameters: {'x': 2.0237637939993616}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,357] Trial 113 finished with value: 0.41401191531647225 and parameters: {'x': 2.64343757686078}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,491] Trial 114 finished with value: 1.0780010753234492 and parameters: {'x': 0.9617316939617923}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,531] Trial 115 finished with value: 0.11280005505949792 and parameters: {'x': 2.335857194443558}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,570] Trial 116 finished with value: 1.1469465213228784 and parameters: {'x': 3.0709558913993042}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,609] Trial 117 finished with value: 0.3711371773047353 and parameters: {'x': 1.3907897101125628}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,652] Trial 118 finished with value: 5.881590578570266 and parameters: {'x': 4.425199080193266}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,691] Trial 119 finished with value: 3.970026333263318 and parameters: {'x': 3.992492492649174}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,730] Trial 121 finished with value: 7.493220969835469e-06 and parameters: {'x': 1.9972626251681884}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,769] Trial 122 finished with value: 0.006590569985776249 and parameters: {'x': 1.9188176744249326}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,810] Trial 124 finished with value: 0.5334382126739019 and parameters: {'x': 2.7303685457862366}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,853] Trial 127 finished with value: 0.6276891197182424 and parameters: {'x': 1.2077316617974423}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,897] Trial 129 finished with value: 0.1849901269210865 and parameters: {'x': 1.56989521402211}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,937] Trial 131 finished with value: 4.5660211588831485 and parameters: {'x': -0.13682501831178207}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,976] Trial 133 finished with value: 6.6687870165096164e-06 and parameters: {'x': 1.99741760053119}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,018] Trial 135 finished with value: 0.3900193839191453 and parameters: {'x': 2.6245153192029362}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,064] Trial 137 finished with value: 2.689290932256982 and parameters: {'x': 0.36009423067757274}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,104] Trial 139 finished with value: 1.0657521578414715 and parameters: {'x': 3.032352729371832}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,143] Trial 141 finished with value: 0.019159615135854288 and parameters: {'x': 2.1384182615692535}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,186] Trial 142 finished with value: 0.05592380842492982 and parameters: {'x': 1.7635178475551911}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,229] Trial 144 finished with value: 2.9340532716316834 and parameters: {'x': 3.712907840962754}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,269] Trial 146 finished with value: 1.1408566938564662 and parameters: {'x': 0.9318910664841034}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,315] Trial 148 finished with value: 0.644364433764054 and parameters: {'x': 2.802723136432515}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,357] Trial 150 finished with value: 0.22696022501623372 and parameters: {'x': 1.523596573253053}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,398] Trial 152 finished with value: 8.967267105719848e-07 and parameters: {'x': 2.0009469565515756}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,440] Trial 154 finished with value: 0.14306252088061894 and parameters: {'x': 2.3782360650184207}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,482] Trial 156 finished with value: 1.2348639470014704 and parameters: {'x': 0.8887556762793025}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,524] Trial 158 finished with value: 0.00032436344803176033 and parameters: {'x': 2.018010092949004}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,567] Trial 160 finished with value: 140.9301434413341 and parameters: {'x': -9.871400230863001}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,606] Trial 162 finished with value: 0.0026742555961396836 and parameters: {'x': 1.9482867947605287}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,650] Trial 164 finished with value: 0.6339095694629374 and parameters: {'x': 2.7961843815743546}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,695] Trial 167 finished with value: 0.42929262218273045 and parameters: {'x': 1.3447957401063921}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,735] Trial 169 finished with value: 0.17806543933570693 and parameters: {'x': 1.5780219918814407}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,775] Trial 171 finished with value: 0.037896464140556085 and parameters: {'x': 2.1946701418825088}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,817] Trial 173 finished with value: 1.5223932052791564 and parameters: {'x': 3.2338529917616428}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,857] Trial 175 finished with value: 0.290744573141532 and parameters: {'x': 2.539207356349607}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,896] Trial 177 finished with value: 0.02766837432573868 and parameters: {'x': 1.8336618674935339}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,937] Trial 179 finished with value: 2.1872268563266273 and parameters: {'x': 0.5210723965228632}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,979] Trial 181 finished with value: 0.7823993768157357 and parameters: {'x': 2.884533423232687}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,020] Trial 183 finished with value: 0.5405174165350208 and parameters: {'x': 1.2648011040983393}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,059] Trial 185 finished with value: 0.0994018533615889 and parameters: {'x': 1.684719405352012}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,099] Trial 187 finished with value: 0.8687966783206724 and parameters: {'x': 1.0679073660195182}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,138] Trial 189 finished with value: 0.0002836859288255196 and parameters: {'x': 1.9831570213790577}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,178] Trial 191 finished with value: 0.1855522620052402 and parameters: {'x': 1.5692422235115886}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,217] Trial 193 finished with value: 0.014176259706242946 and parameters: {'x': 2.119064099149336}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,257] Trial 195 finished with value: 0.3031056524427506 and parameters: {'x': 2.5505503178118696}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,301] Trial 197 finished with value: 0.7046129614229018 and parameters: {'x': 1.1605877285726032}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,340] Trial 199 finished with value: 0.034083001959654864 and parameters: {'x': 1.8153841773854287}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,378] Trial 201 finished with value: 2.5094345956731267e-05 and parameters: {'x': 1.9949905742887302}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,419] Trial 203 finished with value: 0.1935127592804492 and parameters: {'x': 1.560099148352212}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,468] Trial 206 finished with value: 0.3032111968852336 and parameters: {'x': 2.5506461630532202}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,510] Trial 208 finished with value: 0.01226931288899112 and parameters: {'x': 2.1107669304846493}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,553] Trial 210 finished with value: 1.6907824312552262 and parameters: {'x': 0.6996990997252881}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,596] Trial 212 finished with value: 0.06369449317387742 and parameters: {'x': 1.7476223203730619}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,635] Trial 214 finished with value: 0.0074891188640891365 and parameters: {'x': 1.9134603046914935}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,675] Trial 216 finished with value: 0.5586993957109773 and parameters: {'x': 1.2525380305922065}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,722] Trial 218 finished with value: 0.10112943650723834 and parameters: {'x': 2.3180085478524726}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,765] Trial 220 finished with value: 0.0012095839950953366 and parameters: {'x': 2.034779074097729}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,805] Trial 222 finished with value: 0.08061852334380404 and parameters: {'x': 2.2839340123053313}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,844] Trial 224 finished with value: 0.17464908517125038 and parameters: {'x': 1.5820896206466626}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,889] Trial 226 finished with value: 0.38218753513316966 and parameters: {'x': 2.6182131793590053}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,936] Trial 229 finished with value: 8.243269074216567e-06 and parameters: {'x': 1.9971288906196007}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,975] Trial 231 finished with value: 0.0026519229447711803 and parameters: {'x': 2.051496824608622}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,016] Trial 233 finished with value: 0.003438821774903834 and parameters: {'x': 1.9413585319513245}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,058] Trial 235 finished with value: 45.32974830506156 and parameters: {'x': 8.732737058957639}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,110] Trial 237 finished with value: 0.08717649089635421 and parameters: {'x': 2.295256652586109}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,153] Trial 239 finished with value: 0.07637628361768985 and parameters: {'x': 1.7236374055381412}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,198] Trial 241 finished with value: 0.015724766821392906 and parameters: {'x': 2.125398432292405}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,241] Trial 243 finished with value: 0.5511882227518219 and parameters: {'x': 1.2575794838827379}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,284] Trial 245 finished with value: 0.3087294331243194 and parameters: {'x': 2.5556342620144292}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,326] Trial 247 finished with value: 0.08751040622288915 and parameters: {'x': 1.7041784216408662}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,373] Trial 249 finished with value: 0.0054003492325126875 and parameters: {'x': 2.0734870684713487}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,414] Trial 251 finished with value: 0.27456716065656794 and parameters: {'x': 1.476008434555891}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,453] Trial 253 finished with value: 0.31684905754005177 and parameters: {'x': 2.5628934690863376}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,495] Trial 255 finished with value: 0.039455975189218194 and parameters: {'x': 1.801364718166137}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,537] Trial 257 finished with value: 0.11114923212798275 and parameters: {'x': 2.3333905099548917}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,578] Trial 259 finished with value: 1.414530951701149 and parameters: {'x': 3.1893405532904144}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,617] Trial 261 finished with value: 0.44871967092597514 and parameters: {'x': 1.3301345874535877}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,656] Trial 263 finished with value: 0.1363559090273534 and parameters: {'x': 1.6307359900730192}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,695] Trial 265 finished with value: 0.6706066686629844 and parameters: {'x': 2.8189057752043176}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,734] Trial 267 finished with value: 0.012606426121036103 and parameters: {'x': 2.1122783421726385}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,773] Trial 269 finished with value: 0.30508547419154053 and parameters: {'x': 1.4476545698645271}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,812] Trial 271 finished with value: 0.3768308671535154 and parameters: {'x': 2.6138655122691903}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,852] Trial 273 finished with value: 1.8829817534126145 and parameters: {'x': 3.3722178228738375}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,891] Trial 275 finished with value: 0.028317340028438664 and parameters: {'x': 1.8317224315945864}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,931] Trial 277 finished with value: 1.2097485712665843 and parameters: {'x': 0.900114291725461}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,970] Trial 279 finished with value: 0.13126307013386035 and parameters: {'x': 2.362302456704147}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,010] Trial 281 finished with value: 0.02148428042327362 and parameters: {'x': 1.853424830127086}. Best is trial 152 with value: 8.967267105719848e-07.
'''

'''
Process2の実行結果
[I 2024-10-21 09:05:22,732] Trial 120 finished with value: 0.05434891194753381 and parameters: {'x': 2.2331285309599274}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,771] Trial 123 finished with value: 0.010467745551631668 and parameters: {'x': 1.8976879989853015}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,810] Trial 125 finished with value: 1.6779373311507824 and parameters: {'x': 3.295352203514852}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,848] Trial 126 finished with value: 0.8724338844604174 and parameters: {'x': 1.0659583068939495}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,887] Trial 128 finished with value: 0.20685937091029033 and parameters: {'x': 1.5451820464072572}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,925] Trial 130 finished with value: 0.130247060628031 and parameters: {'x': 2.3608975763676323}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:22,963] Trial 132 finished with value: 0.001654859562548494 and parameters: {'x': 1.9593200348752793}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,002] Trial 134 finished with value: 0.35722115802217136 and parameters: {'x': 2.597679812292645}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,050] Trial 136 finished with value: 1.748669073602887 and parameters: {'x': 0.677627483043115}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,090] Trial 138 finished with value: 1.2086120511489098 and parameters: {'x': 3.099368933137966}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,158] Trial 140 finished with value: 0.014854565560317643 and parameters: {'x': 2.121879307350828}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,201] Trial 143 finished with value: 0.07556926740150764 and parameters: {'x': 1.725101350673548}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,241] Trial 145 finished with value: 0.4879785249966954 and parameters: {'x': 1.3014454029950877}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,287] Trial 147 finished with value: 0.11433918360312008 and parameters: {'x': 2.3381407748307206}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,327] Trial 149 finished with value: 2.023846810280485 and parameters: {'x': 3.4226196998075364}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,367] Trial 151 finished with value: 0.3169064886623468 and parameters: {'x': 1.437055519023104}. Best is trial 102 with value: 2.1031661413949087e-06.
[I 2024-10-21 09:05:23,406] Trial 153 finished with value: 0.00020316015987207695 and parameters: {'x': 1.9857465737497233}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,444] Trial 155 finished with value: 0.15930499691996708 and parameters: {'x': 2.3991303006788223}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,487] Trial 157 finished with value: 1.1728547085835355 and parameters: {'x': 0.9170158317946031}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,525] Trial 159 finished with value: 0.0010111847788595292 and parameters: {'x': 1.9682008682687793}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,568] Trial 161 finished with value: 0.0023538872282694648 and parameters: {'x': 1.9514831242940205}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,607] Trial 163 finished with value: 0.0030931450954369225 and parameters: {'x': 1.9443839493002522}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,650] Trial 165 finished with value: 0.5348252753327353 and parameters: {'x': 2.7313174928392834}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,688] Trial 166 finished with value: 46.869863683350374 and parameters: {'x': -4.846156855006345}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,725] Trial 168 finished with value: 0.16936754620829916 and parameters: {'x': 1.588457114982777}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,762] Trial 170 finished with value: 0.0498801314549362 and parameters: {'x': 2.2233386026976443}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,799] Trial 172 finished with value: 0.6573322085731541 and parameters: {'x': 1.1892397342166094}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,841] Trial 174 finished with value: 0.27981958571713605 and parameters: {'x': 2.5289797592698005}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,879] Trial 176 finished with value: 0.014269668601927646 and parameters: {'x': 1.8805442818366251}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,922] Trial 178 finished with value: 2.848103906010479 and parameters: {'x': 0.31236736639442797}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:23,962] Trial 180 finished with value: 0.8075186666154092 and parameters: {'x': 2.8986204241031968}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,001] Trial 182 finished with value: 0.00147435918497243 and parameters: {'x': 2.038397385131965}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,040] Trial 184 finished with value: 0.030962675875407405 and parameters: {'x': 2.1759621433019256}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,077] Trial 186 finished with value: 0.10879134537575276 and parameters: {'x': 2.329835330696626}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,115] Trial 188 finished with value: 0.0008474949193371784 and parameters: {'x': 1.9708882340051797}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,153] Trial 190 finished with value: 0.004004698081287265 and parameters: {'x': 1.9367173161023707}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,192] Trial 192 finished with value: 0.2721268746170443 and parameters: {'x': 1.4783421862781654}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,230] Trial 194 finished with value: 0.011108860859540838 and parameters: {'x': 2.10539858091806}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,268] Trial 196 finished with value: 0.19907910021303704 and parameters: {'x': 2.4461828103065346}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,307] Trial 198 finished with value: 0.7303645569016769 and parameters: {'x': 1.1453863113068707}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,344] Trial 200 finished with value: 1.6173550896541966 and parameters: {'x': 3.2717527627861465}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,382] Trial 202 finished with value: 0.0026278878139372104 and parameters: {'x': 1.9487370717385633}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,420] Trial 204 finished with value: 0.18553751875012345 and parameters: {'x': 1.5692593370134142}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,459] Trial 205 finished with value: 0.457939348465904 and parameters: {'x': 2.6767121607196844}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,497] Trial 207 finished with value: 0.04349257065375798 and parameters: {'x': 2.20854872489123}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,535] Trial 209 finished with value: 1.0370392730503624 and parameters: {'x': 3.0183512522947877}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,573] Trial 211 finished with value: 0.0005225650002660552 and parameters: {'x': 1.9771403193314943}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,610] Trial 213 finished with value: 0.1634669784388846 and parameters: {'x': 2.404310497562065}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,648] Trial 215 finished with value: 0.03624130190305607 and parameters: {'x': 1.8096285160454537}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,692] Trial 217 finished with value: 0.4264164643543551 and parameters: {'x': 1.3469942845928873}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,731] Trial 219 finished with value: 0.5705820086164327 and parameters: {'x': 2.755368789808285}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,771] Trial 221 finished with value: 0.00014777611109750036 and parameters: {'x': 2.012156319800725}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,810] Trial 223 finished with value: 0.07607728220052988 and parameters: {'x': 2.2758211054298236}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,848] Trial 225 finished with value: 0.15213537525429977 and parameters: {'x': 1.609954649746597}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,891] Trial 227 finished with value: 0.6140258167957572 and parameters: {'x': 2.7835979943796163}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,930] Trial 228 finished with value: 1.1193719410742324 and parameters: {'x': 0.9419962471360357}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:24,970] Trial 230 finished with value: 0.0021502376713062724 and parameters: {'x': 2.046370655282261}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,012] Trial 232 finished with value: 0.03461521853936396 and parameters: {'x': 1.8139483444326174}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,050] Trial 234 finished with value: 0.30530299568581254 and parameters: {'x': 1.4474576978313674}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,089] Trial 236 finished with value: 0.12201548593669939 and parameters: {'x': 2.3493071512819332}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,130] Trial 238 finished with value: 1.0174321174999041 and parameters: {'x': 3.0086784014243113}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,169] Trial 240 finished with value: 0.07350677309533114 and parameters: {'x': 1.7288786745839952}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,213] Trial 242 finished with value: 0.006694339303562202 and parameters: {'x': 2.0818189422051043}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,254] Trial 244 finished with value: 0.4165674338026461 and parameters: {'x': 1.3545796456551389}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,295] Trial 246 finished with value: 0.30042835672839396 and parameters: {'x': 2.5481134524242166}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,336] Trial 248 finished with value: 3.176649900372321e-06 and parameters: {'x': 2.0017823158811985}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,383] Trial 250 finished with value: 0.00022293644335404396 and parameters: {'x': 2.014931056337515}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,422] Trial 252 finished with value: 0.7312965077907407 and parameters: {'x': 2.8551587617458765}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,461] Trial 254 finished with value: 0.9889813218925374 and parameters: {'x': 1.005524599654402}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,504] Trial 256 finished with value: 0.01314216140405602 and parameters: {'x': 1.8853607335854943}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,559] Trial 258 finished with value: 0.1664041584661781 and parameters: {'x': 2.4079266581950463}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,603] Trial 260 finished with value: 18.450776104139706 and parameters: {'x': -2.295436660473497}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,643] Trial 262 finished with value: 0.009234458534795922 and parameters: {'x': 2.096096090111908}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,682] Trial 264 finished with value: 1.2238381140580452 and parameters: {'x': 0.8937278300264238}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,722] Trial 266 finished with value: 0.01971927964896053 and parameters: {'x': 2.140425352586207}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,761] Trial 268 finished with value: 0.31827253783796505 and parameters: {'x': 1.4358435165328993}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,801] Trial 270 finished with value: 0.5875507982094772 and parameters: {'x': 2.7665186222196283}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,841] Trial 272 finished with value: 2.203270802008865 and parameters: {'x': 3.484341875043908}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,880] Trial 274 finished with value: 0.05310627127734561 and parameters: {'x': 1.7695520204528892}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,923] Trial 276 finished with value: 0.8523870487251631 and parameters: {'x': 1.0767519029398636}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:25,962] Trial 278 finished with value: 0.219125929570352 and parameters: {'x': 2.4681088864466814}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,001] Trial 280 finished with value: 0.0019087663789001395 and parameters: {'x': 1.9563105690252192}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,040] Trial 282 finished with value: 0.33714898307595076 and parameters: {'x': 1.4193546839283462}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,079] Trial 283 finished with value: 1.0819394935360331 and parameters: {'x': 3.0401632052404244}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,117] Trial 284 finished with value: 0.08193608675698281 and parameters: {'x': 2.2862448021484107}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,155] Trial 285 finished with value: 0.2150334983239724 and parameters: {'x': 1.5362829544604033}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,200] Trial 286 finished with value: 2.0401395527742308 and parameters: {'x': 0.5716654618842858}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,254] Trial 287 finished with value: 0.009231331889643134 and parameters: {'x': 2.09607982040805}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,308] Trial 288 finished with value: 0.3895996896459428 and parameters: {'x': 2.624179212763404}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,359] Trial 289 finished with value: 0.5837888540111726 and parameters: {'x': 1.235939234084636}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,414] Trial 290 finished with value: 0.06300136607895196 and parameters: {'x': 1.7489992707601192}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,469] Trial 291 finished with value: 0.11353127913940411 and parameters: {'x': 2.3369440296835724}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,527] Trial 292 finished with value: 0.9126535367915721 and parameters: {'x': 2.9553290201765945}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,584] Trial 293 finished with value: 8.406327210567766e-05 and parameters: {'x': 1.9908313974834941}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,639] Trial 294 finished with value: 19.85161050727163 and parameters: {'x': 6.455514617557845}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,698] Trial 295 finished with value: 0.1295842128169337 and parameters: {'x': 1.640021927310935}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,751] Trial 296 finished with value: 0.04287332888950258 and parameters: {'x': 2.20705875709446}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,806] Trial 297 finished with value: 0.7568101298598892 and parameters: {'x': 1.1300516510390464}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,864] Trial 298 finished with value: 0.4661093863906172 and parameters: {'x': 2.6827220418227444}. Best is trial 152 with value: 8.967267105719848e-07.
[I 2024-10-21 09:05:26,919] Trial 299 finished with value: 0.006325126362469784 and parameters: {'x': 1.9204693369669925}. Best is trial 152 with value: 8.967267105719848e-07.
'''