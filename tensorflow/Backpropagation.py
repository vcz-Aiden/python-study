import time
import numpy as np

def _t(x):
    return np.transpose(x)

def _m(A, B):
    return np.matmul(A, B)

class Sigmoid:
    def __init__(self):
        self.last_o = 1

    def __call__(self, x):
        self.last_o =  (1.0 / (1.0 + np.exp(-x)))
        return self.last_o

    def grad(self):
        return self.last_o * (1 - self.last_o)

class MeanSquaredError:
    def __init__(self):
        self.dh = 1
        self.last_diff = 1

    def __call__(self, h, y):
        self.last_diff = h - y
        return 1 / 2 * np.mean(np.square(self.last_diff))

    def grad(self):
        return self.last_diff

class Dense:
    def __init__(self, W, b, a_obj):
        self.W = W
        self.b = b
        self.a = a_obj()

        self.dW = np.zeros_like(self.W)
        self.db = np.zeros_like(self.b)
        self.dh = np.zeros_like(_t(self.W))

        self.last_x = np.zeros((self.W.shape[0],))
        self.last_h = np.zeros((self.W.shape[1],))

    def __call__(self, x):
        self.last_x = x
        self.last_h = self.a(_m(_t(self.W), x) + self.b)
        return self.last_h

    def grad(self):
        return self.W * self.a.grad()

    def grad_W(self, dh):
        grad = np.ones_like(self.W)
        grad_a = self.a.grad()
        for j in range(grad.shape[1]):
            grad[:, j] = dh[j] * grad_a[j] * self.last_x
        return grad

    def grad_b(self, dh):
        return dh * self.a.grad()

class DNN:
    def __init__(self, hidden_depth, num_neuron, num_input, num_output, activation=Sigmoid):
        def init_var(i, o):
            return np.random.normal(0.0, 0.01, (i,o)), np.zeros((o,))

        self.sequence = list()

        # First hidden layer
        W, b = init_var(num_input, num_neuron)
        self.sequence.append(Dense(W, b, activation))

        # Hidden layers
        for _ in range(hidden_depth - 1):
            W, b = init_var(num_neuron, num_neuron)
            self.sequence.append(Dense(W, b, activation))

        #Output layer
        W, b = init_var(num_neuron, num_output)
        self.sequence.append(Dense(W, b, activation))

    def __call__(self, x):
        for layer in self.sequence:
            x = layer(x)
        return x

    def calc_gradient(self, loss_obj):
        loss_obj.dh = loss_obj.grad()
        self.sequence.append(loss_obj)

        # back-prop loop
        for j in range(len(self.sequence) -1, 0, -1):
            l1 = self.sequence[j]
            l0 = self.sequence[j - 1]

            l0.dh = _m(l0.grad(), l1.dh)
            l0.dW = l0.grad_W(l1.dh)
            l0.db = l0.grad_b(l1.dh)

        self.sequence.remove(loss_obj)

def gradient_descent(network, x, y, loss_obj, alpha=0.01):
    loss = loss_obj(network(x), y)
    network.calc_gradient(loss_obj)
    for layer in network.sequence:
        layer.W += -alpha * layer.dW
        layer.b += -alpha * layer.db
    return loss

if __name__ == '__main__':
    x = np.random.normal(0.0, 1.0, (10,))
    y = np.random.normal(0.0, 1.0, (2,))

    dnn = DNN(hidden_depth=5, num_neuron=32, num_input=10, num_output=2, activation=Sigmoid)
    loss_obj = MeanSquaredError()

    t = time.time()
    for epoch in range(100):
        loss = gradient_descent(dnn, x, y, loss_obj, 0.01)
        print('Epoch {}: Test {}'.format(epoch, loss))
    print('{} seconds elapsed.'.format(time.time() - t))