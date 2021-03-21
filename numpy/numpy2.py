import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    #indexing and slicing
    x = np.arange(10)
    x = x.reshape((2, 5))

    print(x[1, 3])
    print(x[:, 1:3])
    print(x[0, 0:4])


    #changing data shape of ndarray
    x = np.arange(15).reshape(3, 5)
    y = np.arange(15).reshape(3, 5)

    temp = np.ravel(x)
    print(x)
    temp[0] = 100
    print(x)
    print(temp)

    temp2 = y.flatten()
    print(temp2)
    temp2[0] = 100
    print(y)
    print(temp2)

    #ravel
    x = np.ravel(x, order='F')
    y = y.flatten(order='F')
    print(x)
    print(y)

    y = y.reshape(5, -1)
    print(y)