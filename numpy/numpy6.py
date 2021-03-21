import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    #그래프 그리기
    x = np.linspace(0, 10, 11)
    y = x ** 2 + x + 2 + np.random.randn(11)

    print(x)
    print(y)

    plt.subplot(2, 2, 1)

    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.title("x-y relation")
    plt.grid(True)

    plt.xlim(0, 20)
    plt.ylim(0, 200)

    plt.plot(x, y, linestyle="--", color="#00ff00", marker="^", linewidth=1)

    plt.subplot(2, 2, 2)
    plt.plot(x, y)
    plt.show()

    #plt.scatter(x, y)
    #plt.show()

    data = np.random.randint(1, 100, size=200)
    plt.hist(data, bins=20, alpha=0.3)
    plt.xlabel('data')
    plt.ylabel("number")
    plt.grid()
    plt.show()