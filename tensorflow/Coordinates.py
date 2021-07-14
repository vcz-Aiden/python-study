import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense

# Can CNN return the coordinates?

EPOCHS = 10
size = 10000
v_size = 1000
lenght = 100

def MyModel():
    return tf.keras.models.Sequential([
        Conv2D(32, (3, 3), padding='same', activation='relu'),  #valid / same
        MaxPool2D(),
        Conv2D(64, (3, 3), padding='same', activation='relu'),  # valid / same
        MaxPool2D(),
        Conv2D(128, (3, 3), padding='same', activation='relu'),  # valid / same
        Conv2D(256, (3, 3), padding='same', activation='relu'),  # valid / same
        Flatten(),
        Dense(128, activation='relu'),
        Dense(2, activation='relu')
    ])

if __name__ == '__main__':
    x_train = []
    y_train = []
    x_test, y_test = [], []

    for i in range(size) :
        x, y = np.random.randint(lenght, size=2)
        temp_data = np.zeros((lenght, lenght))
        temp_data[x][y] = 1
        x_train.append(temp_data)
        y_train.append([x, y])

    for i in range(v_size) :
        x, y = np.random.randint(lenght, size=2)
        temp_data = np.zeros((lenght, lenght))
        temp_data[x][y] = 1
        x_test.append(temp_data)
        y_test.append([x, y])

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)

    x_train = x_train.astype(np.float32)
    x_test = x_test.astype(np.float32)

    x_train = x_train[..., np.newaxis]
    x_test = x_test[..., np.newaxis]

    print(x_train[0].shape)
    print(y_train[0].shape)
    print(x_test[0].shape)
    print(y_test[0].shape)

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32).prefetch(2048)
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32).prefetch(2048)

    model = MyModel()

    model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)

    while True:
        a = input("test")
        x, y = np.random.randint(lenght, size=2)
        print("x: ", x, "  y: ", y)
        temp_data = np.zeros((lenght, lenght))
        temp_data[x][y] = 1
        x_train = []
        x_train.append(temp_data)
        x_train = np.array(x_train)
        x_train = x_train.astype(np.float32)
        x_train = x_train[..., np.newaxis]
        print(model.predict(x_train))