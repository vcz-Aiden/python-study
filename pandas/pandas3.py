import pandas as pd
import numpy as np

if __name__ == "__main__" :
    #dictionary
    train_data = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6],
        "c": [123, 234, 168]
    }, index=['x', 'y', 'z'])

    print(train_data)

    print(train_data.shape)
    print(train_data.describe())
    print(train_data.info())

    #with Series
    a = pd.Series([100, 200, 300], ['a', 'b', 'c'])
    b = pd.Series([200, 100, 300], ['a', 'b', 'd'])
    c = pd.Series([300, 200, 100], ['a', 'b', 'c'])

    print(pd.DataFrame([a, b, c], index=[100, 101, 102]))

    pd.DataFrame([a, b, c], index=[100, 101, 102]).to_csv("test.csv", mode='w', index=None)


