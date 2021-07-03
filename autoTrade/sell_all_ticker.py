import pyupbit
import pandas as pd
import time
from datetime import datetime,timedelta

def sell_all_ticker(hours):

    start_time = datetime.now()
    tomorrow = start_time+timedelta(hours=hours)

    while(1):

        now = datetime.now()
        if now > tomorrow:
            print("start_time :",start_time)
            print("end_time :",now)
            break

        time.sleep(120)

    access = ""
    secret = ""
    upbit = pyupbit.Upbit(access, secret)

    sell_order = pd.read_csv("uuid.csv")

    unsell_list = []
    unsell_list_balance = []

    for i in range(len(sell_order)):

        try:
            upbit.cancel_order(sell_order['uuid'].iloc[i])
        except:
            continue

        unsell_list.append(sell_order['market'].iloc[i])
        unsell_list_balance.append(sell_order['volume'].iloc[i])

    for i in range(len(unsell_list)):

        upbit.sell_market_order(ticker=unsell_list[i], volume=unsell_list_balance[i])
        time.sleep(0.2)