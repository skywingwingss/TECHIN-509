import logic
import Board
from Database import Database
import random

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

    def run(self):
        if self.mode=="GUI":
            while self.game_not_over():
                if not logic.moveChess(self.board,self.get_current_player()):
                    continue
                self.winner=logic.check_winner(self.board)
                self.other_player()
                self.turn+=1
                if self.is_draw():
                    break
            self.end()
        else:
            while self.game_not_over():
                if not logic.moveChess(self.board,self.get_current_player()):
                    continue
                self.winner=logic.check_winner(self.board)
                self.other_player()
                self.turn+=1
                if self.is_draw():
                    break
            self.end()


    def is_draw(self):
        if self.turn==9:
            return True
        else:
            return False

    def end(self):
        print(self.board)
        winnerName =None
        if self.winner==None:
            print("Draw!")
        else:
            self.other_player()
            print("Player{} win the game!".format(self.currentplayer.get_name()))
            if self.winner=="X":
                winnerName=self.playerX.name
            elif self.winner=="0":
                winnerName=self.playerO.name
        self.database.record_game(self.playerX.name,self.playerO.name,winnerName)
        print(self.database.get_globalrank())


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

    def get_move(self,board):
        instream = input("Player{} please choose a position in format x,y to place chess:".format(self.chess))
        return logic.getInput(instream,board)

    def get_chess(self):
        return self.chess

    def get_name(self):
        return self.name

class AI():
    def __init__(self,chess):
        self.chess=chess
        self.name="AI"
        self.nextMove=(0,0)

    def get_move(self,board):
        x=random.randint(0,2)
        y=random.randint(0,2)
        round=0
        while not logic.board_movable(x,y,board):
            if round%2==0:
                x=logic.roundadd(x,0,2)
            else:
                y=logic.roundadd(y,0,2)
            round+=1
        return x,y

    def get_chess(self):
        return self.chess

    def get_name(self):
        return self.name





if __name__ == '__main__':
    database=Database()
    database.record_game("a","c","c")
    print(database.get_globalrank())



