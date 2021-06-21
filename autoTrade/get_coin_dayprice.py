import pybithumb
import time
from datetime import datetime,date
import pandas as pd
import os

# 모든 종목 현재가 얻기
def get_coin_dayprice():

    try:
        if not os.path.exists("coin"):
            os.makedirs("coin")
    except OSError:
        print("Error: Creating directory")


    dont_buy = ['KMD','ADX','LBC','IGNIS','DMT','EMC2','TSHP','LAMB','EDR','PXL','PICA','RDD','RINGX'\
                ,'VITE','ITAM','SYS','NXT','BFT','NCASH','FSN','PI','RCN','PRO','ANT','BASIC','CON','BTT','NEO']

    tickers = pybithumb.get_tickers()
    name_dic = {'name':[]}
    name_list = []

    for ticker in tickers :

        df = pybithumb.get_ohlcv(ticker)
        df = df.reset_index()

        flag = datetime(2021,1,1)

        if df['time'].iloc[0]  < flag :

            if ticker in dont_buy:
                continue
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