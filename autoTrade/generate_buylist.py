import pyupbit
import pandas as pd

def generate_buylist():

    dic = pd.read_csv("dic.csv")

    pre_list = {'ticker':[],'predict':[],'close':[], 'bef_close':[]}
    all_ticker = []
    all_predict = []
    all_close = []
    all_bef_close = []

    dic = pd.DataFrame(dic)
    dic_ticker = dic['ticker'].tolist()
    dic = dic.set_index('ticker')

    for ticker in dic_ticker:

        close = dic['close'].loc[ticker]
        predict = dic['predict'].loc[ticker]
        bef_close = dic['bef_close'].loc[ticker]

        if predict > close  and  predict > bef_close:

            all_ticker.append(ticker)
            all_predict.append(predict)
            all_close.append(close)
            all_bef_close.append(bef_close)

    print("bef:",all_ticker)

    pre_list['ticker'] = all_ticker
    pre_list['predict'] = all_predict
    pre_list['close'] = all_close
    pre_list['bef_close'] = all_bef_close
    pre_list = pd.DataFrame(pre_list)
    pre_list['ticker'] = pre_list['ticker'].apply(lambda x: "KRW-" + x[:-4])

    pre_list_tickerlist = pre_list['ticker'].tolist()
    pre_list = pre_list.set_index('ticker')

    ret_list = {'ticker': [], 'predict': [], 'close': [], 'bef_close':[]}
    ret_ticker = []
    ret_predict = []
    ret_close = []
    ret_bef_close = []

    access = ""
    secret = ""
    upbit = pyupbit.Upbit(access, secret)
    available_tickerlist = pyupbit.get_tickers("KRW")

    pre_list_tickerlist = [x for x in pre_list_tickerlist if x in available_tickerlist]

    for ticker in pre_list_tickerlist:
        ret_ticker.append(ticker)
        ret_close.append(pre_list['close'].loc[ticker])
        ret_predict.append(pre_list['predict'].loc[ticker])
        ret_bef_close.append(pre_list['bef_close'].loc[ticker])
    ret_list['ticker'] = ret_ticker
    ret_list['predict'] = ret_predict
    ret_list['close'] = ret_close
    ret_list['bef_close'] = ret_bef_close
    print("aft:",ret_ticker)
    print("predict:",ret_predict)
    print("close:",ret_close)
    print("bef_close:",ret_bef_close)

    df = pd.DataFrame(ret_list)
    df.to_csv("pre_list.csv")