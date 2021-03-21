import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    x = np.arange(15).reshape(3, 5)
    y = np.random.rand(15).reshape(3, 5)
    print(x)
    print(y)

    print(np.add(x, y))       #shape of array must be same
    print(np.subtract(x, y))
    print(x * y)
    print(x / y)

    print(np.mean(y))
    print(np.max(y))
    print(np.argmax(y))
    print(np.var(y))
    print(np.median(y))
    print(np.std(y))

    print(np.sum(y))
    print(np.sum(y, axis=1))
    print(np.cumsum(y))

    z = np.random.randn(10)
    print(z)

    print(z > 0)
    print(np.any(z > 0))
    print(np.all(z > 0))

    print(np.where(z > 0, z, 0))