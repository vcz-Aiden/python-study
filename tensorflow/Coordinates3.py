import tensorflow as tf
from tensorflow import feature_column
import numpy as np
import pandas as pd
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense

# Can CNN return the coordinates?

EPOCHS = 50
size = 11000
coord = 10
v_size = 1000
lenght = 5000

def MyModel():
    return tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(256, activation='tanh'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(256, activation='tanh'),
        tf.keras.layers.Dense(2, activation='relu')
    ])

if __name__ == '__main__':
    x_train = []
    y_train = []
    x_test, y_test = [], []

    for i in range(size) :
        temp_data = []
        total = 0
        ans_x, ans_y = 0, 0

        for c in range(coord):
            x, y = np.random.randint(lenght, size=2)
            z = np.random.randint(1, lenght, size=1)[0]
            temp_data += [x * z, y * z]
            total += z
            ans_x += x * z
            ans_y += y * z

        print(temp_data)
        print([ans_x / total, ans_y / total])
        y_train.append([ans_x / total / 100, ans_y / total / 100])
        x_train.append(temp_data / total)

    x_temp, y_temp = x_train[10000:], y_train[10000:]

    x_train = np.array(x_train[:10000])
    y_train = np.array(y_train[:10000])
    x_test = np.array(x_temp)
    y_test = np.array(y_temp)

    print(x_train[0])
    print(y_train[0])
    print(x_test[0])
    print(y_test[0])

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(True).batch(32)
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

    model = MyModel()

    model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)

    while True:
        a = input("test")
        temp_data = []
        total = 0
        ans_x, ans_y = 0, 0
        x_train = []

        for c in range(coord):
            x, y = np.random.randint(lenght, size=2)
            z = np.random.randint(1, lenght, size=1)[0]
            temp_data += [x * z, y * z]
            total += z
            ans_x += x * z
            ans_y += y * z

        x_train.append(temp_data / total)
        x_train = np.array(x_train)
        print(temp_data)
        print(model.predict(x_train))
        print([ans_x / total / 100, ans_y / total / 100])