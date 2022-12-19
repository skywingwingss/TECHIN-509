import logic
import Board
from Database import Database

class Tictactoe():
    def __init__(self,playerX,playerO,mode="CLI"):
        self.mode=mode#determine run in web or cli
        self.CHESS=[None,"X","O"]
        self.board=Board.Board()
        self.winner=None
        self.playerX=playerX
        self.playerO=playerO
        self.currentplayer=self.playerX
        self.turn=0
        self.database=Database()

    def game_not_over(self):
        self.winner=logic.check_winner(self.board)
        if self.winner==None:
            return True
        else:
            return False

    def get_current_player(self):
        return self.currentplayer

    def get_board(self):
        return self.board.get_wholeboard()

    def run(self):
        while self.game_not_over():
            if not logic.moveChess(self.board,self.get_current_player()):
                continue
            self.winner=logic.check_winner(self.board)
            self.other_player()
            self.turn+=1
            if self.is_draw():
                break



    def is_draw(self):
        if self.turn==9:
            return True
        else:
            return False

    def end(self):
        winnerName =None
        hint=""
        if self.winner==None:
            hint="Draw!"
        else:
            #self.other_player()
            if self.winner=="X":
                winnerName=self.playerX.name
            elif self.winner=="0":
                winnerName=self.playerO.name
            hint="Player{} win the game!".format(self.currentplayer.get_name())
        self.database.record_game(self.playerX.name,self.playerO.name,winnerName)
        return hint


    def other_player(self):
        """Given the character for a player, returns the other player."""
        if self.currentplayer==self.playerX:
            self.currentplayer=self.playerO
        elif self.currentplayer==self.playerO:
            self.currentplayer=self.playerX


class Human():
    def __init__(self,chess,name):
        self.chess=chess
        self.name=name
        self.nextMove=(0,0)


    def get_move(self,board):
        return self.nextMove

    def get_chess(self):
        return self.chess

    def get_name(self):
        return self.name