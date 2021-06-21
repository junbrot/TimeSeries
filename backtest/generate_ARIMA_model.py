import pandas as pd
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import os

def generate_ARIMA_model():

    tickerlist = pd.read_csv("tickerlist.csv")

    try:
        if not os.path.exists("predict_data"):
            os.makedirs("predict_data")
    except OSError:
        print("Error: Creating directory")

    for i in range(len(tickerlist)):

        all_data = pd.read_csv("./coin/" + tickerlist['name'].iloc[i])
        training_data = pd.read_csv("./training_data/" + tickerlist['name'].iloc[i])
        test_data = pd.read_csv("./test_data/" + tickerlist['name'].iloc[i])

        # 종목별 모델 생성
        model = auto_arima(training_data['close'], trace=True, error_action='ignore', start_p=1, start_q=1, max_p=3,
                                 max_q=3, suppress_warnings=True, stepwise=False, seasonal=False, with_intercept=False)

        order = (model.order[0], model.order[1], model.order[2])

        dic = {'time': [], 'predict': [],'close': [],'high':[]}
        time_data = []
        predict_data = []

        # 위에서 생성한 모델과 test_data를 사용해 predict_data를 생성
        for day in range(len(training_data), len(training_data) + len(test_data)):

            model = ARIMA(all_data['close'].iloc[0:day], order=order)
            model_fit = model.fit()

            forecast_data = model_fit.forecast(steps=1)
            predict_data.append(round(forecast_data[day],2))
            time_data.append(all_data['time'].iloc[day])
            print(all_data['time'].iloc[day])

        print(predict_data)
        print(len(predict_data))

        dic['time'] = time_data
        dic['predict'] = predict_data
        dic['close'] = test_data['close']
        dic['high'] = test_data['high']

        df = pd.DataFrame(dic)
        df.to_csv("predict_data/" + tickerlist['name'].iloc[i])

