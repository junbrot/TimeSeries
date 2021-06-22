from get_coin_dayprice import get_coin_dayprice
from generate_ARIMA_order import generate_ARIMA_order
from generate_predict_data import generate_predict_data
from generate_buylist import generate_buylist
from generate_buysell_order import generate_buysell_order
from sell_all_ticker import sell_all_ticker

if __name__ == '__main__':

    sell_all_ticker(3)

    while(1):

        # 1. coin 일봉 업데이트
        get_coin_dayprice()
        # 2. order 업데이트 (1주일에 한번)
        generate_ARIMA_order()
        # 3. ARIMA 모델을 사용해 predict data 생성
        generate_predict_data()
        # 4. 살 종목 추리기
        generate_buylist()
        # 5. 매수 주문, 매도 주문 넣기
        generate_buysell_order()
        # 6. 6시간 후 전체 매도
        sell_all_ticker(4)

