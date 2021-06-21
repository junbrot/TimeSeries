import pandas as pd
from datetime import datetime, date, timedelta
import numpy as np

def backtest():

    tickerlist = pd.read_csv("tickerlist.csv")

    win_list = []
    lose_list = []
    cagr_list = []

    df = pd.read_csv("./predict_data/BTC.csv")
    bitcoin_predict = df['predict']
    bitcoin_close = df['close']

    for ticker in range(len(tickerlist)):

        df = pd.read_csv("./predict_data/" + tickerlist['name'].iloc[ticker])
        df['time'] = df['time'].apply(lambda x: datetime(int(x[:4]), int(x[5:7]), int(x[8:10])))
        df['time'].index = df['time']

        win = 0
        lose = 0
        cagr = 1

        for i in range(1,len(df)):

            check_1 = df['predict'].iloc[i] > df['close'].iloc[i-1]

            if check_1:

                buy_price = df['close'].iloc[i-1]
                high_price = df['high'].iloc[i]
                close_price = df['close'].iloc[i]
                predict_price = df['predict'].iloc[i]

                if high_price > buy_price * 1.01:
                    cagr = cagr * 1.01
                    win = win+1
                else:
                    cagr = cagr * close_price/buy_price
                    if(close_price > buy_price):
                        win+=1
                    else:
                        lose+=1

        if win > 0 and lose > 0 :
            cagr = cagr**(1.0/(win+lose))
            print(tickerlist['name'].iloc[ticker])
            print("승률 :",win/(win+lose))
            print("cagr :",cagr)

            win_list.append(win)
            lose_list.append(lose)
            cagr_list.append(cagr)

    cagr = cagr_list[0]
    for i in range(1,len(cagr_list)):
        cagr *= cagr_list[i]

    cagr = cagr**(1.0/len(cagr_list))

    print("평균 승률 :",np.sum(win_list)/(np.sum(win_list)+np.sum(lose_list)))
    print("평균 cagr :",cagr)

