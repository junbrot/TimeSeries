from get_dayprice import collect_dayprice_everyday
from generate_training_test_data import generate_training_test_data
from generate_ARIMA_model import generate_ARIMA_model
from backtest import backtest
if __name__ == '__main__':

    collect_dayprice_everyday()
    generate_training_test_data()
    generate_ARIMA_model()
    backtest()