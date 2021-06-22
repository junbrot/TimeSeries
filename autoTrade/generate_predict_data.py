import pandas as pd
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

def generate_predict_data():

    tickerlist = pd.read_csv("tickerlist.csv")
    order = pd.read_csv("order.csv")
    order = order.set_index('ticker')

    dic = {'ticker': [], 'predict': [],'bef_close':[], 'close': []}
    ticker = []
    predict = []
    close = []
    bef_close = []

    for i in range(len(tickerlist)):

        try:
            all_data = pd.read_csv("coin/" + tickerlist['name'].iloc[i])
            all_data['time'] = all_data['time'].apply(lambda x: datetime(int(x[:4]), int(x[5:7]), int(x[8:10])))

            name = tickerlist['name'].iloc[i]
            first = int(order['first'].loc[name])
            second = int(order['second'].loc[name])
            third = int(order['third'].loc[name])
            temp_order =  (first,second,third)

            model = ARIMA(all_data['close'], order= temp_order)
            model_fit = model.fit()
            forecast_data = model_fit.forecast(steps=1)

            print(all_data['time'].iloc[-1])
            print("name :",tickerlist['name'].iloc[i])
            print("close :", all_data['close'].iloc[-1])
            print("predict :", round(forecast_data[len(all_data['close'])], 2))
            print()

            ticker.append(tickerlist['name'].iloc[i])
            predict.append(round(forecast_data[len(all_data['close'])], 2))
            close.append(all_data['close'].iloc[-1])
            bef_close.append(all_data['close'].iloc[-2])

        except:
            continue

    dic['ticker'] = ticker
    dic['predict'] = predict
    dic['close'] = close
    dic['bef_close'] = bef_close

    df = pd.DataFrame(dic)
    df.to_csv("dic.csv")

    return dic