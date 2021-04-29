import pandas as pd
import numpy as np

if __name__ == "__main__" :
    data = pd.read_csv('./train.csv', sep=",", index_col=0)  #, usecols=['playbackTime'])
    print(data)

    print(data[['playbackTime', 'curTime']])   #column 선택
    print(data[:10])    #row 선택

    print(data.info())

    data.index = np.arange(100, 3560)

    print(data.head())

    print(data.loc[[986, 100, 101]])     #use the given index
    print(data.iloc[[0, 986, 100]])    #zero-based index

    print(data.loc[[100, 200, 300], ['playbackTime', 'curHP', 'maxHP']])


    #making mask
    print(data['isDead'] == True)
    print((data['curHP'] < 200) & (data['isDead'] == False))

    print(data[(data['curHP'] < 200) & (data['isDead'] == False)])