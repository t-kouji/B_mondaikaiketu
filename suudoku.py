suudoku = [
    [   1,    7,    2,    9,    5, None, None,    8,    6],
    [   9, None, None,    4,    8, None, None,    3,    7],
    [   8, None,    3, None,    1,    7,    9,    5, None],
    [None, None,    6, None, None,    8,    7,    4, None], 
    [   3,    1, None,    5, None, None,    2, None, None],
    [None, None,    4,    7,    9,    1,    5,    6, None], 
    [None,    2, None,    1, None, None,    8, None,    5],
    [None, None, None, None, None, None,    6,    1,    9],
    [None, None, None, None,    7, None,    3, None, None]
]

from pprint import pprint

"""
gr1～gr9までを辞書として取得。key"ij"に番地、valueに値を得る。
"""
gr1 = {}
for i in range(0,3):
    gr1["0{}".format(i)] = suudoku[0][i]
for i in range(0,3):
    gr1["1{}".format(i)] = suudoku[1][i]
for i in range(0,3):
    gr1["2{}".format(i)] = suudoku[2][i]

gr2 = {}
for i in range(3,6):
    gr2["0{}".format(i)] = suudoku[0][i]
for i in range(3,6):
    gr2["1{}".format(i)] = suudoku[1][i]
for i in range(3,6):
    gr2["2{}".format(i)] = suudoku[2][i]

gr3 = {}
for i in range(6,9):
    gr3["0{}".format(i)] = suudoku[0][i]
for i in range(6,9):
    gr3["1{}".format(i)] = suudoku[1][i]
for i in range(6,9):
    gr3["2{}".format(i)] = suudoku[2][i]

gr4 = {}
for i in range(0,3):
    gr4["3{}".format(i)] = suudoku[3][i]
for i in range(0,3):
    gr4["4{}".format(i)] = suudoku[4][i]
for i in range(0,3):
    gr4["5{}".format(i)] = suudoku[5][i]

gr5 = {}
for i in range(3,6):
    gr5["3{}".format(i)] = suudoku[3][i]
for i in range(3,6):
    gr5["4{}".format(i)] = suudoku[4][i]
for i in range(3,6):
    gr5["5{}".format(i)] = suudoku[5][i]

gr6 = {}
for i in range(6,9):
    gr6["3{}".format(i)] = suudoku[3][i]
for i in range(6,9):
    gr6["4{}".format(i)] = suudoku[4][i]
for i in range(6,9):
    gr6["5{}".format(i)] = suudoku[5][i]

gr7 = {}
for i in range(0,3):
    gr7["6{}".format(i)] = suudoku[6][i]
for i in range(0,3):
    gr7["7{}".format(i)] = suudoku[7][i]
for i in range(0,3):
    gr7["8{}".format(i)] = suudoku[8][i]

gr8 = {}
for i in range(3,6):
    gr8["6{}".format(i)] = suudoku[6][i]
for i in range(3,6):
    gr8["7{}".format(i)] = suudoku[7][i]
for i in range(3,6):
    gr8["8{}".format(i)] = suudoku[8][i]

gr9 = {}
for i in range(6,9):
    gr9["6{}".format(i)] = suudoku[6][i]
for i in range(6,9):
    gr9["7{}".format(i)] = suudoku[7][i]
for i in range(6,9):
    gr9["8{}".format(i)] = suudoku[8][i]

for i in range(1,10):
    exec("print(gr{})".format(i))


def get_suudoku():
    #数独リストの行列リストを取得
    return [[suudoku[i][j]for j in range(9)] for i in range(9) ]


def get_suudoku_r():
    #数独リストの行列を反対にしたリストを取得
    return [[suudoku[j][i]for j in range(9)] for i in range(9) ]

"""
gr1からgr9まで順番にkeyに対してのvalueをforループで取得し、
valueにNoneがでたらsuudokuの行と列とgrの中に1～9があるかどうか調べる。
もしあったらリストに格納し、リスト内に格納される数字が1個だけだったら、suudokuに書き込む。
これをNoneがなくまるまでforループで繰り返す。
"""

for a in suudoku:
    if None in a:
        for i in range(1,10):
            for k in eval("gr{}".format(i)):
                if eval("gr{}".format(i))[k] == None:
                    l = [none for none in range(1,10) if
                         not(none in get_suudoku()[int(k[0])])
                         and not (none in get_suudoku_r()[int(k[1])])
                         and not (none in eval("gr{}".format(i)).values())]
                    if len(l) == 1:
                        suudoku[int(k[0])][int(k[1])] = l[0]
        pprint(suudoku)
# pprint(suudoku)
