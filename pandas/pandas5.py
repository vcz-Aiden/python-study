import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    data = pd.read_csv('./train.csv', sep=",", index_col=0)  #, usecols=['playbackTime'])
    print(data)

    data['double_cur'] = data['curHP'] * 2

    print(data)

    data.insert(2, 'time', data['curTime'] / 60)

    print(data)

    data.drop('double_cur', axis=1, inplace=True)

    print(data)

    print(data.corr())

    plt.matshow(data.corr())
    plt.show()