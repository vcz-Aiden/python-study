import numpy as np
import pandas as pd

if __name__ == "__main__" :
    x = pd.Series([1, 2, 3])
    print(x)

    y = pd.Series(["a", "b", "c"])
    print(y)

    z = pd.Series(np.arange(200))
    print(z)

    x = pd.Series([1, 2, 3], [100, 200, 300])
    print(x)

    y = pd.Series(np.arange(5), np.arange(100, 105), dtype=np.int32)
    print(y)

    print(y.index)
    print(y.values)
    print(y[103])

    y[105] = 90
    print(y)

    ###############
    s = pd.Series([1, 1, 4,2,3,6,76,2,6,7,3,3,23,5,77,2,3,1,3,45, np.NaN])
    print(s)

    print(len(s))
    print(s.size)
    print(s.shape)
    print(s.unique())
    print(s.count())
    print(s.mean())
    print(s.value_counts())

    print(s[[5, 7, 8]])

    print(s.head())
    print(s.tail())