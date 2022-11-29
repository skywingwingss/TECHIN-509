import logic
import Board
import random
import pandas as pd
import os

class Tictactoe():
    def __init__(self,playerX,playerO):
        self.CHESS=[None,"X","O"]
        self.board=Board.Board()
        self.winner=None
        self.playerX=playerX
        self.playerO=playerO
        self.currentplayer=self.playerX
        self.turn=0

    def game_not_over(self):
        self.winner=logic.check_winner(self.board)
        if self.winner==None:
            return True
        else:
            return False

    def get_current_player(self):
        return self.currentplayer

    def run(self):
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
        if self.winner==None:
            print("Draw!")
        else:
            self.other_player()
            print("Player{} win the game!".format(self.currentplayer.get_chess()))

    def other_player(self):
        """Given the character for a player, returns the other player."""
        if self.currentplayer==self.playerX:
            self.currentplayer=self.playerO
        elif self.currentplayer==self.playerO:
            self.currentplayer=self.playerX

class Human():
    def __init__(self,chess):
        self.chess=chess

    def get_move(self,board):
        instream = input("Player{} please choose a position in format x,y to place chess:".format(self.chess))
        return logic.getInput(instream,board)

    def get_chess(self):
        return self.chess

class AI():
    def __init__(self,chess):
        self.chess=chess

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

class Database():
    def __init__(self):
        self.datapath="./data/database.csv"
        self.check_localfile()
        self.df=self.load_data()


    def check_localfile(self):
        #check existing local file and create one if failed to find.
        if not os.path.exists("./data"):
            os.mkdir("./data")
        if not os.path.exists(self.datapath):
            data={"player":["a"],
                  "win":[1],
                  "lose":[0],
                  "draw":[0],
                  "score":[1]}
            df=pd.DataFrame(data)
            df.to_csv(self.datapath,index=None)

    def load_data(self):
        df=pd.read_csv(self.datapath)
        return df

    def write_data(self):
        self.df.to_csv(self.datapath)

    def add_record(self,player,result):
        if not( player in self.df["player"]):
            self.df.loc[len(self.df)]=[player,0,0,0,0]
        p=self.df.loc[player]
        #self.df.loc[len(self.df)]=[player1,player2,winner]

    def sort_record(self):
        self.df



if __name__ == '__main__':
    database=Database()
    database.add_record("a","win")



