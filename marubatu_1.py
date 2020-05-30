import random

win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #勝ちパターン
l_board = ["０","１","２","３","４","５","６","７","８"]
l_remaining = [0,1,2,3,4,5,6,7,8]
l_self = []
l_com = []
p = 0

"""
範囲外の数字指定でIndexError
番号重複でValueError
"""
print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(l_board[0],l_board[1],l_board[2],l_board[3],
                                            l_board[4],l_board[5],l_board[6],l_board[7],l_board[8]))
try:
    while True:
        if p == 0:
            while True: #０～８以外の数字を入れないようにする。
                #"●"にしたい場所を番号でinputし、ans_self変数に格納
                ans_self = int(input("あなたの番です。\"●\"をしたい場所の番号を(半角整数で)入力してください。"))
                # l_self.append(ans_self) #l_selfリストに追加
                # l_self.sort() #l_selfリストを昇順でソートする
                if (0 <= ans_self < 9) and (ans_self in l_remaining) :
                    break
                else:
                    print("\"●\"又は\"×\"が入っていない場所を0～8の整数（半角）で入力し直してください。")
            l_board[ans_self]="●" #上記で指定した番号をl_boradの対応するインデックス番号へ"●"で書き込む
            l_remaining.remove(ans_self) #指定した番号をl_remainingリストから削除する
            print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(l_board[0],l_board[1],l_board[2],l_board[3],
                                                        l_board[4],l_board[5],l_board[6],l_board[7],l_board[8]))
            #p = 0
            for i in win:
                for j in i:
                    if l_board[j]=="●":
                        p+=1
                if p == 3:
                    print("あなたの勝ちです！")
                    break
                else:
                    p = 0
            # print(l_remaining)
            # print(l_self)

            if p < 3:
                #p = 0
                ans_com = random.choice(l_remaining) #l_remainingリストからランダムに数字をchoiceし、ans_com変数に格納
                # l_com.append(ans_com) #l_comリストに追加
                # l_com.sort() #l_comリストを昇順でソートする
                l_board[ans_com]="×" #上記で指定した番号をl_boradの対応するインデックス番号へ"×"で書き込む
                l_remaining.remove(ans_com) #指定した番号をl_remainingリストから削除する
                print("コンピューターの番です。\n{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(l_board[0],l_board[1],l_board[2],l_board[3],
                                                            l_board[4],l_board[5],l_board[6],l_board[7],l_board[8]))
                for i in win:
                    for j in i:
                        if l_board[j]=="×":
                            p+=1
                    if p == 3:
                        print("あなたの負けです…")
                        break
                    else:
                        p = 0
            else:
                break #あなたの勝ちでループを抜ける。
        else:
            break #comの勝ちでループをぬける。
except IndexError :
    print("引き分けです。")
except ValueError:
	print("正しい値が入力されなかったので最初からやり直してください。")
