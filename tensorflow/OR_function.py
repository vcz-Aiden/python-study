import tensorflow as tf
import numpy as np

def v(*args):
    return np.array(args)

class Perceptron:
    def __init__(self, w, b):
        self.w = tf.Variable(w, dtype=tf.float32)
        self.b = tf.Variable(b, dtype=tf.float32)

    def __call__(self, x):
        return tf.sign(tf.reduce_sum(self.w * x) + self.b)

if __name__ == '__main__':
    w = v(1, 1)
    b = 0.5

    perceptron = Perceptron(w, b)

    p1 = perceptron(v(1, 1)) # T, T
    p2 = perceptron(v(-1, 1)) # F, T
    p3 = perceptron(v(-1, -1)) # F, F
    p4 = perceptron(v(1, -1)) # T, F

    print(p2.numpy(), p1.numpy())
    print(p3.numpy(), p4.numpy())
