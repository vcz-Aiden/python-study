import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    #creating numpy
    x = np.array([1, 2, 3])
    y = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    print(type(y))

    x = np.arange(10)
    y = np.arange(1, 10)
    z = np.arange(1, 10, 2)
    print(x)
    print(y)
    print(z)

    x = np.ones((2, 3))
    y = np.zeros((2, 3, 4))
    print(x)
    print(y)

    x = np.empty((3, 4))
    y = np.full((3, 4), 5)
    print(x)
    print(y)

    x = np.eye(5)
    print(x)

    x = np.linspace(1, 10, 4)
    print(x)

    x = x.reshape((2, 2))
    print(x)



    #random submodule
    x = np.random.rand(2, 3)       #random value [0, 1]
    print(x)

    x = np.random.randn(3, 4)      #random value with normal distribution
    print(x)

    x = np.random.randint(1, 100, size=(3, 5))    #random int value between low and high
    print(x)

    #np.random.seed(100)      #when we want to make fixed random value

    x = np.random.choice(np.array([1, 2, 3, 1.5, 2.6, 4.9]), size=(3, 4), replace=True)     #sampling from given 1d array
    print(x)

    #get random value from specific function
    np.random.uniform(10, 100, size=(2, 5))
    np.random.normal(size=(2,3))