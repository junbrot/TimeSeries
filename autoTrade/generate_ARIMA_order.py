import pandas as pd
from datetime import datetime
from pmdarima import auto_arima

def generate_ARIMA_order():

    tickerlist = pd.read_csv("tickerlist.csv")

    ord = {'ticker': [], 'first': [], 'second': [], 'third': []}
    every_ticker = []
    first = []
    second = []
    third = []

    for i in range(len(tickerlist)):

        try:
            all_data = pd.read_csv("coin/" + tickerlist['name'].iloc[i])
            all_data['time'] = all_data['time'].apply(lambda x: datetime(int(x[:4]), int(x[5:7]), int(x[8:10])))

            model = auto_arima(all_data['close'], trace=True, error_action='ignore', start_p=1, start_q=1, max_p=3,
                               max_q=3, suppress_warnings=True, stepwise=False, seasonal=False, with_intercept=False)

            every_ticker.append(tickerlist['name'].iloc[i])
            first.append(model.order[0])
            second.append(model.order[1])
            third.append(model.order[2])

            if i%10 == 0:

                ord['ticker'] = every_ticker
                ord['first'] = first
                ord['second'] = second
                ord['third'] = third

                df = pd.DataFrame(ord)
                df.to_csv("order.csv")

        except:
            pass