import tensorflow as tf
import numpy as np

def v(*args):
    return np.array(args)

def xor(x):
    h1 = p_nand(x)
    h2 = p_or(x)
    return p_and(v(h1, h2))

class Perceptronn:
    def __init__(self, w, b):
        self.w = tf.Variable(w, dtype=tf.float32)
        self.b = tf.Variable(b, dtype=tf.float32)

    def __call__(self, x):
        return tf.sign(tf.reduce_sum(self.w * x) + self.b)

if __name__ == '__main__':
    p_nand = Perceptronn(w=v(-1, -1), b=0.5)
    p_or = Perceptronn(w=v(1, 1), b=0.5)
    p_and = Perceptronn(w=v(1, 1), b=-0.5)

    p1 = xor(v(1, 1))  # T, T
    p2 = xor(v(-1, 1))  # F, T
    p3 = xor(v(-1, -1))  # F, F
    p4 = xor(v(1, -1))  # T, F

    print(p2.numpy(), p1.numpy())
    print(p3.numpy(), p4.numpy())

