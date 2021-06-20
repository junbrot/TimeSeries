from get_dayprice import get_dayprice
from generate_training_test_data import generate_training_test_data
from generate_ARIMA_model import generate_ARIMA_model
from backtest import backtest
if __name__ == '__main__':

    # 1. 가상화폐 가격데이터 불러오기
    get_dayprice()
    # 2. 가상화폐 가격데이터를 training 데이터와 test 데이터로 나눔
    # generate_training_test_data()
    # 3. ARIMA 모델 생성
    # generate_ARIMA_model()
    # 4. backtest
    # backtest()