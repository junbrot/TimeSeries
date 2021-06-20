import pybithumb
import time
from datetime import datetime,date
import pandas as pd

# 모든 종목 현재가 얻기
def collect_dayprice_everyday():

    tickers = pybithumb.get_tickers()
    name_dic = {'name':[]}
    name_list = []

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