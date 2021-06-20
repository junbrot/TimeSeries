import pandas as pd
from datetime import datetime,date
import os
def generate_training_test_data():

    tickerlist = pd.read_csv("tickerlist.csv")

    try:
        if not os.path.exists("training_data"):
            os.makedirs("training_data")
    except OSError:
        print("Error: Creating directory")

    try:
        if not os.path.exists("test_data"):
            os.makedirs("test_data")
    except OSError:
        print("Error: Creating directory")

    for i in range(len(tickerlist)):

        df = pd.read_csv("./coin/"+tickerlist['name'].iloc[i])
        df['time'] = df['time'].apply(lambda x: datetime(int(x[:4]),int(x[5:7]),int(x[8:10])))

        flag = datetime(2021,1,1)

        cnt = 0
        for j in range(len(df)):

            if flag == df['time'].iloc[j]:
                cnt = j
                break

        training_data = df[:cnt]
        test_data = df[cnt:]

        training_data.to_csv("./training_data/"+tickerlist['name'].iloc[i])
        test_data.to_csv("./test_data/"+tickerlist['name'].iloc[i])

    print(training_data.tail())
    print(test_data.head())
