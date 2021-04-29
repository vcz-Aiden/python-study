import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

if __name__ == "__main__" :
    df1 = pd.DataFrame({'key1': np.arange(10), 'value1': np.random.randn(10)})
    df2 = pd.DataFrame({'key1': np.arange(10), 'value1': np.random.rand(10)})
    df3 = pd.DataFrame({'key2': np.arange(10), 'value2': np.random.rand(10)})

    print(df3)

    print(pd.concat([df1, df2], ignore_index=True))
    print(pd.concat([df1, df2], axis=1))

    print(pd.concat([df1, df3]))
    print(pd.concat([df1, df3], axis=1))

    #merge and join
