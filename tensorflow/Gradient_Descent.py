import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.1*x**4 - 1.5*x**3 + 0.6*x**2 + 1.0*x + 20.0

def df_dx(x):
    return 0.4*x**3 - 4.5*x**2 + 1.2*x + 1.0

def gradientDescent(x, eps=1e-5, lr=0.01, max_epoch=1000):
    min_x = x
    min_y = f(min_x)

    x_log = [x]

    for _ in range(max_epoch):
        grad = df_dx(x)
        new_x = x - lr * grad
        y = f(new_x)

        x_log.append(new_x)

        if min_y > y:
            min_x = new_x
            min_y = y

        if (np.abs(x - new_x) < eps):
            break

        x = new_x

    return min_x, min_y, x_log

if __name__ == '__main__':
    min_x1, min_y1, x_log1 = gradientDescent(5)
    min_x2, min_y2, x_log2 = gradientDescent(-5)
    min_x3, min_y3, x_log3 = gradientDescent(0.5)
    min_x4, min_y4, x_log4 = gradientDescent(15, lr=0.005)

    y_log1 = f(np.array(x_log1))
    y_log2 = f(np.array(x_log2))
    y_log3 = f(np.array(x_log3))
    y_log4 = f(np.array(x_log4))

    plt.plot(x_log1, y_log1, '.-')
    plt.plot(x_log2, y_log2, '.-')
    plt.plot(x_log3, y_log3, '.-')
    plt.plot(x_log4, y_log4, '.-')
    plt.show()