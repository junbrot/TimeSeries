from get_coin_dayprice import get_coin_dayprice
from generate_ARIMA_order import generate_ARIMA_order
from generate_predict_data import generate_predict_data
from generate_buylist import generate_buylist
if __name__ == '__main__':

    get_coin_dayprice()
    generate_ARIMA_order()
    generate_predict_data()
    generate_buylist()