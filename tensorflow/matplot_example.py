import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def DrawQuiver():
    X = np.arange(-10, 10, 1)
    Y = np.arange(-10, 10, 1)
    U, V = np.meshgrid(X, Y)

    fig, ax = plt.subplots()
    q = ax.quiver(X, Y, U, V)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiver key, length = 10', labelpos='E')

    plt.show()

def Draw3DSurface():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def DrawMatrix():
    A = np.random.rand(5, 5)
    print(A)

    fig, axs = plt.subplots(1, 3, figsize=(10, 3))
    for ax, interp in zip(axs, ['nearest', 'bilinear', 'bicubic']):
        ax.imshow(A, interpolation=interp)
        ax.set_title(interp.capitalize())
        ax.grid(True)

    plt.show()

if __name__ == '__main__':
    DrawQuiver()