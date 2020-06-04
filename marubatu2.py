"""Ver3 com知能強化"""
import random

win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #勝ちパターン
l_board = ["０","１","２","３","４","５","６","７","８"]
l_remaining = [0,1,2,3,4,5,6,7,8] #残っている番地
l_com = [] #comが取得した番地
l_self = [] #selfが取得した番地

"""盤面の表示"""
def display_of_board(x):
    if x == 0:
        print("マルバツゲームです。先行は1/2の確率で決まります。")
    
    print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(l_board[0],l_board[1],l_board[2],l_board[3],
                                                    l_board[4],l_board[5],l_board[6],l_board[7],l_board[8]))
    
"""先攻決め"""
def first_player():
    first_player = random.randrange(2)
    if first_player == 0:
        return "self"
    elif first_player == 1:
        return "com"
    
"""
comの知能強化のためにすること
取得した番地（l_com）と残っている番地（l_remaining）とwinの関係。
相手の番地（l_self）と残っている番地（l_remaining）とwinの関係。
ジャッジの時と同様にwinの中の×の個数をカウントする。1個だったらそれを選ぶ。
2個ならどちらかを選ぶ。
最初の一手はランダム。
"""

def com_intelligence():
    """winの各要素の中でl_comの要素とかぶってない要素を調べ、リストに格納"""
    potential_com = [[w for w in wi if w not in l_com] for wi in win]

    """winの各要素の中でl_selfの要素とかぶってない要素を調べ、リストに格納"""
    potential_self = [[w for w in wi if w not in l_self] for wi in win]
    
    """potential_comの各要素の要素数を調べ1こだったらその値がcomの勝ち手"""
    for i in potential_com:
        if (len(i) == 1) and (i[0] in l_remaining):
            print("com勝ちの一手")
            return i[0]

    """そうじゃなかったらpotential_selfの各要素の要素数を調べ１こだったらその値が守り手"""
    for i in potential_self:
        if (len(i) == 1) and (i[0] in l_remaining):
            print("com守りの一手")
            return i[0]

    """そうじゃなかったらpotential_comの各要素の要素数を調べ2こだったらその値を選択"""
    for i in potential_com:
        if len(i) == 2:
            for j in i:
                if j in l_remaining:
                    print("com繋ぎの一手")
                    return j
    
    """そうじゃなかったらpotential_selfの各要素の要素数を調べ2こだったらその値を選択"""
    for i in potential_self:
        if len(i) == 2:
            for j in i:
                if j in l_remaining:
                    print("com繋ぎの一手")
                    return j
        
    """そうじゃなかったらl_remainingの中からランダムに選ぶ""" 
    print("com最初の一手")
    return random.choice(l_remaining)

      
"""番地の選択"""  
def select(player):
    if player == "self":
        print("私の番です。\"●\"をしたい場所の番号を(半角整数で)入力してください。")
        while True: #０～８以外の数字を入れないようにする。
            try:         
                my_ans = int(input()) #"●"にしたい場所を番地でinputし、my_ans変数に格納
                if (0 <= my_ans < 9) and (my_ans in l_remaining) :
                    l_self.append(my_ans)
                    return my_ans
                else:
                    print("\"●\"又は\"×\"が入っていない場所を0～8の整数（半角）で入力し直してください。")
            except ValueError:
                print("0～8の整数（半角）で入力し直してください。")
    elif player == "com":
        print("コンピューターの番です。")
        com_ans = com_intelligence()
        l_com.append(com_ans)
        return com_ans    


        
"""盤面に書き込み、l_remainingから選択した数字を削除"""        
def writing2board(player):
    if player == "self":
        l_board[select_number]="●" # select_numberをl_boradの対応するインデックス番号へ"●"で書き込む   
    elif player == "com":
        l_board[select_number]="×" # select_numberをl_boradの対応するインデックス番号へ"×"で書き込む
    l_remaining.remove(select_number) # select_numberをl_remainingリストから削除する

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
    display_of_board(0)
    count = 0 #引き分け判定のための勝負回数カウント
    while True:
        if player == "self":
            select_number = select("self")
            writing2board("self")
            display_of_board(1)
            if jadge("self") == "win":
                print("you winner!")
                break
            else:
                player = "com"
                count += 1

        elif player == "com":
            select_number = select("com")
            writing2board("com")
            display_of_board(1)
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
