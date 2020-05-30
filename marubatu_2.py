import random

win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #勝ちパターン
l_board = ["０","１","２","３","４","５","６","７","８"]
l_remaining = [0,1,2,3,4,5,6,7,8]

"""盤面の表示"""
def display_of_board():
    print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(l_board[0],l_board[1],l_board[2],l_board[3],
                                                l_board[4],l_board[5],l_board[6],l_board[7],l_board[8]))
    
"""先攻決め"""
def first_player():
    first_player = random.randrange(2)
    if first_player == 0:
        return "self"
    elif first_player == 1:
        return "com"
      
"""盤面の選択"""  
def select(player):
    if player == "self":
        print("私の番です。\"●\"をしたい場所の番号を(半角整数で)入力してください。")
        while True: #０～８以外の数字を入れないようにする。
            try:         
                my_ans = int(input()) #"●"にしたい場所を番号でinputし、my_ans変数に格納
                if (0 <= my_ans < 9) and (my_ans in l_remaining) :
                    return my_ans
                else:
                    print("\"●\"又は\"×\"が入っていない場所を0～8の整数（半角）で入力し直してください。")
            except ValueError:
                print("0～8の整数（半角）で入力し直してください。")
    elif player == "com":
        print("コンピューターの番です。")
        com_ans = random.choice(l_remaining) #l_remainingリストからランダムに数字をchoiceし、com_ans変数に格納
        return com_ans

"""盤面に書き込み、l_remainingから選択した数字を削除"""        
def writing2board(player):
    if player == "self":
        l_board[select_number]="●" # my_selectで指定した番号をl_boradの対応するインデックス番号へ"●"で書き込む   
    elif player == "com":
        l_board[select_number]="×" # com_select_mumberをl_boradの対応するインデックス番号へ"×"で書き込む
    l_remaining.remove(select_number) # com_select_mumberをl_remainingリストから削除する

"""ジャッジ"""
def jadge(player):
    if player == "self":
        point = 0
        for i in win:
            for j in i:
                if l_board[j]=="●":
                    point += 1
            if point == 3:
                return "win"
            else:
                point = 0
                
    elif player == "com":
        point = 0
        for i in win:
            for j in i:
                if l_board[j]=="×":
                    point += 1
            if point == 3:
                return "lose"
            else:
                point = 0
        
        
"""関数の実行"""
def main():
    global select_number
    player = first_player()
    display_of_board()
    count = 0 #引き分け判定のための勝負回数カウント
    while True:
        if player == "self":
            select_number = select("self")
            writing2board("self")
            display_of_board()
            if jadge("self") == "win":
                print("you winner!")
                break
            else:
                player = "com"
                count += 1

        elif player == "com":
            select_number = select("com")
            writing2board("com")
            display_of_board()
            if jadge("com") == "lose":
                print("you loser...")
                break
            else:
                player = "self"
                count += 1
        if count == 9:
            print("引き分けです。")
            break

if __name__ == '__main__':
    select_number = 0
    main()