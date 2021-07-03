import pyupbit
import pandas as pd
import time

def generate_buysell_order():

    def get_hoga(price):

        if price < 10.:
            return round(price, 2)
        elif price < 100.:
            return round(price, 1)
        elif price < 1000.:
            return round(price)
        elif price < 10000.:
            return (price // 5) * 5
        elif price < 100000.:
            return (price // 10) * 10
        elif price < 500000.:
            return (price // 50) * 50
        elif price < 2000000.:
            return (price // 100) * 100
        else:
            return (price // 1000) * 1000


    # upbit에서 private api 발급 받아야 사용 가능
    access = ""
    secret = ""
    upbit = pyupbit.Upbit(access, secret)

    pre_list = pd.read_csv("pre_list.csv")
    pre_tickerlist = pre_list['ticker'].tolist()
    pre_list = pre_list.set_index('ticker')

    market_price = 1.015

    ret_all = []

    ticker_sellprice = []
    list_ticker = []
    list_sell_price = []

    # close update
    for ticker in pre_tickerlist:

        current_price = float(pyupbit.get_current_price(ticker))
        close = float(pre_list['close'].loc[ticker])
        predict_price = get_hoga(float(pre_list['predict'].loc[ticker]))
        bef_close = float(pre_list['bef_close'].loc[ticker])

        cond1 = bef_close < predict_price

        if cond1:

            priority = predict_price / close + predict_price / bef_close + predict_price / current_price
            if current_price * market_price < predict_price:
                predict_price = get_hoga(current_price * market_price)
            ticker_tuple = (priority, ticker, predict_price)
            ticker_sellprice.append(ticker_tuple)

        time.sleep(0.2)

    # sorting
    ticker_sellprice.sort(reverse=True)
    # print(ticker_sellprice)
    for (i, ticker, predict_price) in ticker_sellprice:
        list_ticker.append(ticker)
        list_sell_price.append(predict_price)

    print(list_ticker)
    print(list_sell_price)

    current_balance = upbit.get_balances()
    usable_balance = float(current_balance[0]['balance'])
    all_balance = pd.DataFrame(current_balance[1:])
    all_balance = all_balance.set_index('currency')

    usable_balance_per_ticker = usable_balance / 5.1
    usable_balance_per_ticker = int(usable_balance_per_ticker)

    print("매수예상 종목수", len(pre_list))
    # 시장가 매수
    for i in range(min(6, len(pre_list))):
        upbit.buy_market_order(ticker=list_ticker[i], price=usable_balance_per_ticker)
        time.sleep(1)

    # 지정가 매도
    for i in range(min(6, len(pre_list))):
        try:
            current_balance = upbit.get_balances()
            all_balance = pd.DataFrame(current_balance[1:])
            all_balance = all_balance.set_index('currency')
            ticker = str(list_ticker[i])[4:]
            balance = max(all_balance['locked'].loc[ticker], all_balance['balance'].loc[ticker])

            sell_price = list_sell_price[i]
            if sell_price < all_balance['avg_buy_price'].loc[ticker] * 1.01:
                sell_price = get_hoga(all_balance['avg_buy_price'].loc[ticker] * 1.015)

            ret = upbit.sell_limit_order(list_ticker[i], sell_price, balance)
            ret_all.append(ret)
            time.sleep(1)
        except:
            continue

    df = pd.DataFrame(ret_all)
    df.to_csv("uuid.csv")
