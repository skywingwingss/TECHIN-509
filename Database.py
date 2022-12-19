import pandas as pd
import os


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
            data={"player":["test"],
                  "win":[1],
                  "lose":[0],
                  "draw":[0],
                  "score":[1]}
            df=pd.DataFrame(data)
            df.set_index(["player"],inplace=True)
            df.to_csv(self.datapath)

    def load_data(self):
        df=pd.read_csv(self.datapath,index_col=0)
        return df

    def write_data(self):
        self.df.to_csv(self.datapath)

    def add_record(self,player,result):
        #update player record in cache
        if not( player in self.df.index):
            self.df.loc[player]=[0,0,0,0]
        self.df.loc[player][result]+=1#update data
        #calculate score
        playerinfo=self.df.loc[player]
        win=playerinfo["win"]
        lose=playerinfo["lose"]
        score=win-lose
        self.df.loc[player]["score"]=score

        #self.df.loc[len(self.df)]=[player1,player2,winner]
    def record_game(self,player1,player2,winner):
        #record a game and update local database
        if player1==winner:
            self.add_record(player1,"win")
            self.add_record(player2,"lose")
        elif player2==winner:
            self.add_record(player1,"lose")
            self.add_record(player2,"win")
        else:
            self.add_record(player1,"draw")
            self.add_record(player2,"draw")
        self.sort_record()
        self.write_data()

    def sort_record(self):
        self.df.sort_values(by=["score"],ascending=False,inplace=True)

    def get_globalrank(self):
        #return all the records with rank
        output_df=self.df
        output_df.reset_index(inplace=True)
        rank=[i+1 for i in range(len(self.df))]
        output_df.insert(0,"rank",rank)
        return output_df.to_string(index=False)

    def get_record(self,player):
        if not player in self.df.index:
            return None
        return self.df[player]

    def delete_record(self,player):
        self.df.drop(index=player,inplace=True)

    def clear_database(self):
        #reset database
        data = {"player": ["test"],
                "win": [1],
                "lose": [0],
                "draw": [0],
                "score": [1]}
        df = pd.DataFrame(data)
        df.set_index(["player"], inplace=True)
        self.df=df
        self.write_data()