import pandas as pd
import matplotlib.pyplot as plt

folder="./static/"

def update_StatisticalPic():
    #load data
    datapath="./data/database.csv"
    df=pd.read_csv(datapath)
    player=df["player"].to_list()

    #show each player's winning rate
    df_winning_rate=df["win"]/(df["win"]+df["lose"]+df["draw"])
    print(df_winning_rate)
    ax=df_winning_rate.plot(kind="bar")
    xticks_index=[i for i in range(len(df))]
    plt.xticks(xticks_index,player)
    plt.xlabel("Player")
    plt.ylabel("Win Rate")
    fig=ax.get_figure()
    fig.savefig(folder+"win_rate.png")
    plt.show()

    #show the winner makeup
    df_pie=df
    df_pie.set_index(["player"],inplace=True)
    df_pie.plot.pie(y="win")
    plt.savefig(folder+"win_percent.png")
    plt.show()

    #show the detailed record using stack bar

    xticks_index=[i for i in range(len(df))]
    win_list=df["win"].to_list()
    lose_list=df["lose"].to_list()
    draw_list=df["draw"].to_list()
    x=range(len(df))
    rects1=plt.bar(x,height=win_list,width=0.2,color="green",label="Win")
    rects2=plt.bar(x,height=draw_list,width=0.2,color="blue",label="Draw")
    rects3=plt.bar(x,height=lose_list,width=0.2,color="red",label="Lose")
    plt.ylabel("Number")
    plt.xlabel("Player")
    plt.xticks(xticks_index,player)
    plt.legend()
    plt.savefig(folder+"globalstats.png")
    plt.show()

if __name__ =="__main__":
    update_StatisticalPic()

