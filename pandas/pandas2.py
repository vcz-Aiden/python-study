import pandas as pd
import numpy as np

if __name__ == "__main__" :
    #Series data operation
    s = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    s2 = pd.Series([6, 3, 2, 1], ['d', 'c', 'b', 'e'])

    print(s)
    print(s2)

    print(s + s2)
    print(s * s2)
    print(s ** s2)

    #boolean selection
    s = pd.Series(np.arange(10), np.arange(10) + 1)
    print(s[s >= 3])
    print(s[s.index > 5])
    print(s[(s.index > 5) & (s <= 8)])

    #Series change data and slicing
    s = pd.Series(np.arange(100, 105), ['a', 'c', 'b', 'd', 'e'])
    print(s)
    s['a'] = 200
    s['k'] = 300
    print(s)
    temp = s.drop('k') #set inplace as true to apply on s directly
    print(s)
    print(temp)

    s2 = pd.Series(np.arange(100, 105))
    print(s2[1:3])
    print(s[1:3])
    print(s['c':'d'])