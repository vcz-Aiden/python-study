import tensorflow as tf
from tensorflow import feature_column
import numpy as np
import pandas as pd
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense

# Can CNN return the coordinates?

EPOCHS = 10
size = 11000
coord = 10
v_size = 1000
lenght = 5000

class PredCameraModel(tf.keras.Model):
    def __init__(self):
        super(PredCameraModel, self).__init__()

        self.dense1_1 = tf.keras.layers.Dense(32, activation="relu")
        self.dense1_2 = tf.keras.layers.Dense(64, activation="relu")
        self.dense1_3 = tf.keras.layers.Dense(1, activation="relu")
        self.batch_no1 = tf.keras.layers.BatchNormalization()
        self.batch_no2 = tf.keras.layers.BatchNormalization()


        self.dense2_1 = tf.keras.layers.Dense(64, activation='relu')
        self.batch_norm1 = tf.keras.layers.BatchNormalization()
        self.dense2_2 = tf.keras.layers.Dense(128, activation='relu')
        self.dense2_5 = tf.keras.layers.Dense(2, activation='relu')

    def call(self, inputs, training=None, mask=None):
        result_inputs = None

        for c in range(coord):
            z = self.dense1_1(inputs[:, 2 + c * 5:5 + c * 5])
            z = self.batch_no1(z)
            z = self.dense1_2(z)
            z = self.batch_no2(z)
            z = self.dense1_3(z)

            cx = inputs[:, c * 5:2 + c * 5]

            z = tf.keras.layers.concatenate([cx, z], axis=1)

            if (c == 0):
                result_inputs = cx
            else:
                result_inputs = tf.keras.layers.concatenate([result_inputs, cx], axis=1)

        result_inputs = self.dense2_1(result_inputs)
        result_inputs = self.batch_norm1(result_inputs)
        result_inputs = self.dense2_2(result_inputs)
        result_inputs = self.dense2_5(result_inputs)

        return result_inputs

def makeTrainData():
    result_x = []
    result_y = []
    ans_x, ans_y = 0, 0
    total = 0

    for c in range(coord):
        x, y = np.random.randint(lenght, size=2)
        z1, z2, z3 = np.random.randint(1, 100, size=3)
        z = z1 * z2 / 10 + z3 * 2
        total += z

        result_x += [x, y, z1, z2, z3]
        ans_x += x * z
        ans_y += y * z

    result_y = [ans_x / total / 1000, ans_y / total / 1000]
    return (result_x, result_y)


if __name__ == '__main__':
    x_train = []
    y_train = []

    for s in range(size):
        x, y = makeTrainData()

        x_train.append(x)
        y_train.append(y)

    x_val = np.array(x_train[10000:])
    y_val = np.array(y_train[10000:])
    x_train = np.array(x_train[:10000])
    y_train = np.array(y_train[:10000])

    x_train = x_train.astype(np.float32)
    y_train = y_train.astype(np.float32)
    x_val = x_val.astype(np.float32)
    y_val = y_val.astype(np.float32)

    print(x_train.shape)
    print(y_train.shape)
    print(x_val.shape)
    print(y_val.shape)

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(True).batch(32).prefetch(64)
    test_ds = tf.data.Dataset.from_tensor_slices((x_val, y_val)).batch(32).prefetch(64)

    model = PredCameraModel()

    model.compile(optimizer='adam',
                loss='mean_squared_error',
                metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)

    while True:
        a = input("test")
        x_train = []
        y_train = []

        x, y = makeTrainData()

        x_train.append(x)
        y_train.append(y)

        x_train = np.array(x_train).astype(np.float32)

        print(model.predict(x_train))
        print(y_train)
