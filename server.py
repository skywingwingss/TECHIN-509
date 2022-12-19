from flask import Flask, render_template, request, redirect, url_for
from Game_server import Tictactoe
from Game_server import Human
from Gameandplayer import AI
import json
import logic


Game=""

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("index.html")

# @app.route('/Game')
# def start():
#     return render_template("play.html")

@app.route('/index_playinfo',methods=['POST'])
def GameStart():

    player1=request.args.get('player1_name')
    player2=request.args.get('player1_name')
    if player2=="":
        #AI mode
        playerX = Human("X",player1)
        playerO = AI("O")
    else:
        playerX = Human("X", player1)
        playerO = Human("O",player2)
    global Game
    Game= Tictactoe(playerX, playerO)
    return showGameboard()

def showGameboard():
    global Game
    board=Game.get_board()
    p11=board[0][0]
    p12=board[0][1]
    p13=board[0][2]
    p21=board[1][0]
    p22=board[1][1]
    p23=board[1][2]
    p31=board[2][0]
    p32=board[2][1]
    p33=board[2][2]
    return render_template("play.html",chess="X",p_11=p11,p_12=p12,p_13=p13,
                           p_21=p21,p_22=p22,p_23=p23,
                           p_31=p31,p_32=p32,p_33=p33,)
# @app.route('/Game_move', methods=['POST'])
# def Move():
#     if not logic.moveChess(self.board, self.get_current_player()):
#         continue
#     self.winner = logic.check_winner(self.board)
#     self.other_player()
#     self.turn += 1
#     if self.is_draw():
#         break
#     Game.run()
@app.route('/play_move',methods=['POST'])
def Move():
    global Game
    data=request.get_json()
    x=int(data["x"])
    y=int(data["y"])
    print(x,y)
    Game.currentplayer.nextMove=(x,y)
    Game.turn += 1
    logic.moveChess(Game.board, Game.get_current_player())
    win=not Game.game_not_over()

    if win or Game.is_draw():
        return json.dumps({"sta":Game.end(),"chess":Game.currentplayer.get_chess()})

    Game.winner = logic.check_winner(Game.board)
    Game.other_player()

    return {"sta":None,"chess":Game.currentplayer.get_chess()}



if __name__ =="__main__":
    app.run(debug=True, port=8080)
