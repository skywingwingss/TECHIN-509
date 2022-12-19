# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def check_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    #0~2 record 1~3 rows, 3~5 record 1~3 columns, 6,7 record crosses
    board=board.get_wholeboard()
    sameChessSum = [0 for i in range(8)]
    for i in range(3):
        for j in range(3):
            if board[j][i] == "X":
                sameChessSum[j] += 1
            elif board[j][i]=="O":
                sameChessSum[j] -=1

            if board[i][j] == "X":
                sameChessSum[j+3] += 1
            elif board[i][j]=="O":
                sameChessSum[j+3] -=1
        if board[i][i] == "X":
            sameChessSum[6] += 1
        elif board[i][i]=="O":
            sameChessSum[6]-=1

        if board[i][2 - i] == "X":
            sameChessSum[7] += 1
        elif board[i][2-i]=="O":
            sameChessSum[7]-=1
    if 3 in sameChessSum:
        return "X"
    elif -3 in sameChessSum:
        return "O"
    else:
        return None

#Perform a move on the board
def moveChess(board,player):
    print(board)
    x,y=player.get_move(board)
    if (x,y)==(-1,-1):
        return False
    board.set(x,y,player.get_chess())
    return True

# format input
def transferInput(instream):
    try:
        x, y = map(int, instream.split(","))
    except:
        return -1, -1
    # Transfer input coordinate to list index
    return x - 1, y - 1

# check transferred input
def checkInput(x, y, board):

    if not ((x in range(3)) and (y in range(3))):
        # print("Input a wrong coordinate, the input x,y both in range (1,3)!")
        return -1, -1
    elif not board_movable(x,y,board):
        # print("There already is a chess on that position!")
        return -1, -1
    else:
        return x, y

# Get input in string format
def getInput(instream,board):
    x, y = transferInput(instream)
    x, y = checkInput(x, y, board)
    return x, y
#check whether the (x,y) position is empty for a chess
def board_movable(x,y,board):
    if not board.get(x, y) == " ":
        return False
    else:
        return True

#add num with 1, if the result exceeds upbound, it goes to lowbound
def roundadd(num,upbound, lowbound):
    num+=1
    if num>upbound:
        num=lowbound
    return num


################for server#############
#Perform a move on the board
def moveChess_server(board,player,x,y):
    print(board)
    x,y=player.get_move(board)
    if (x,y)==(-1,-1):
        return False
    board.set(x,y,player.get_chess())
    return True


##########################################
#Deprecated
# def switchPlayer(player):
#     if player==1:
#         player=2
#     elif player==2:
#         player=1
#     return player
#
# #Deprecated
# #check whether the player win the game
# def checkWinner(x,y,board):
#     playerChess=board[x][y]
#     sameChessSum=[0,0,0,0]
#     for i in range(3):
#         if board[x][i]==playerChess:
#             sameChessSum[0]+=1
#         if board[i][y]==playerChess:
#             sameChessSum[1]+=1
#         if board[i][i]==playerChess:
#             sameChessSum[2]+=1
#         if board[i][2-i]==playerChess:
#             sameChessSum[3]+=1
#     if 3 in sameChessSum:
#         return True
#     else:
#         return False

# player=1
# while True:
#     if player ==1:
#         instream=input("Player1 please choose a position in format x,y to place chess:")
#         x,y=transferInput(instream)
#         x,y=checkInput(x,y)
#         if (x,y)==(-1,-1):
#             continue
#         board[x][y]="X"
#         printBoard(board)
#         if checkWinner(x,y,board):
#             print("Player1 win the game!")
#             break
#         player=2
#
#     elif player==2:
#         instream=input("Player2 please choose a position in format x,y to place chess:")
#         x,y=transferInput(instream)
#         x,y=checkInput(x,y)
#         if (x,y)==(-1,-1):
#             continue
#         board[x][y] = "O"
#         printBoard(board)
#         if checkWinner(x,y,board):
#             print("Player2 win the game!")
#             break
#         player=1
