import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    #broadcasting
    x = np.arange(15).reshape(3, 5)
    y = np.random.randn(15).reshape(3, 5)

    print(x + 2)

    a = np.arange(12).reshape(4, 3)
    b = np.random.randn(3)

    print(a + b)

    x = np.random.randint(1, 100, size=(10))
    print(x)
    mask = x % 2 == 0
    print(x[mask])
    print(x[x > 30])
    print(x[(x % 2 == 0) | (x > 30)])
    print(x[(x % 2 == 0) & (x > 30)])