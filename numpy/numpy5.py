import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    #linalg submodule
    #역행렬
    x = np.random.randn(3, 3)
    print(x)

    print(np.linalg.inv(x))

    print(np.linalg.inv(x) @ x) #행렬 곱

    a = np.array([[1, 1], [2, 4]])
    b = np.array([25, 64])

    print(a)
    print(b)

    a = np.array([[1, 1, 1], [4, 8, 3], [1, 2, 3]])
    b = np.array([25, 64, 10])

    print(np.linalg.solve(a, b))     #행렬 방정식 해 구하기
    print(np.allclose(a @ np.linalg.solve(a, b), b))    #너무 작은 값 처리