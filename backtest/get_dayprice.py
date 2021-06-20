import pybithumb
import time
from datetime import datetime
import pandas as pd
import os

# 모든 종목 현재가 얻기
def get_dayprice():

    tickers = pybithumb.get_tickers()
    name_dic = {'name':[]}
    name_list = []

    try:
        if not os.path.exists("./coin"):
            os.makedirs("./coin")
    except OSError:
        print("Error: Creating directory")

    for ticker in tickers :

        df = pybithumb.get_ohlcv(ticker)
        df = df.reset_index()

        flag = datetime(2019,1,1)

        if df['time'].iloc[0]  < flag :

            df = df.set_index('time')
            df.to_csv("./coin/"+ticker+".csv")
            name = ticker + ".csv"
            name_list.append(name)
            time.sleep(0.1)

        else :
            print(ticker,df['time'].iloc[0])
            continue

        name_dic['name'] = name_list
        df = pd.DataFrame(name_dic)
        df.to_csv("tickerlist.csv")