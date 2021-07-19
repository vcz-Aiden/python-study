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
lenght = 500

def MyModel():
    return tf.keras.models.Sequential([
        Conv2D(32, (3, 3), padding='same', activation='relu'),  # valid / same
        tf.keras.layers.BatchNormalization(),
        MaxPool2D(),
        Conv2D(64, (3, 3), padding='same', activation='tanh'),  # valid / same
        tf.keras.layers.BatchNormalization(),
        MaxPool2D(),
        Conv2D(128, (3, 3), padding='same', activation='tanh'),  # valid / same
        tf.keras.layers.BatchNormalization(),
        Conv2D(256, (3, 3), padding='same', activation='tanh'),  # valid / same
        Flatten(),
        Dense(128, activation='relu'),
        Dense(2, activation='relu')
    ])

if __name__ == '__main__':
    x_train = []
    y_train = []
    x_test, y_test = [], []

    for i in range(size) :
        temp_data = np.zeros((lenght, lenght, 1))
        total = 0
        ans_x, ans_y = 0, 0

        for c in range(coord):
            x, y = np.random.randint(lenght, size=2)
            z = np.random.randint(1, lenght, size=1)[0]
            temp_data[x][y][0] = z
            total += z
            ans_x += x * z
            ans_y += y * z

        y_train.append([ans_x / total, ans_y / total])
        x_train.append(temp_data)

    x_temp, y_temp = x_train[10000:], y_train[10000:]

    x_train = np.array(x_train[:10000])
    y_train = np.array(y_train[:10000])
    x_test = np.array(x_temp)
    y_test = np.array(y_temp)

    print(x_train.shape)

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(True).batch(32)
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

    model = MyModel()

    model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)

    while True:
        a = input("test")
        x_train = []

        temp_data = np.zeros((lenght, lenght, 1))
        total = 0
        ans_x, ans_y = 0, 0

        for c in range(coord):
            x, y = np.random.randint(lenght, size=2)
            z = np.random.randint(1, lenght, size=1)[0]
            temp_data[x][y][0] = z
            total += z
            ans_x += x * z
            ans_y += y * z

        x_train.append(temp_data)
        x_train = np.array(x_train)
        print(x_train.shape)
        print(model.predict(x_train)[0])
        print([ans_x / total, ans_y / total])