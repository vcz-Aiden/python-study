import pandas as pd
import numpy as np

if __name__ == "__main__" :
    data = pd.read_csv('./train.csv', sep=",", index_col=0, usecols=['playbackTime'])
    print(data)