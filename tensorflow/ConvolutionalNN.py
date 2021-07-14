import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense

EPOCHS = 10

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
        Dense(10, activation='softmax')
    ])

if __name__ == '__main__':
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

    x_train, x_test = x_train / 255.0, x_test / 255.0

    x_train = x_train.astype(np.float32)
    x_test = x_test.astype(np.float32)

    x_train = x_train[..., np.newaxis]
    x_test = x_test[..., np.newaxis]

    print(x_train[0].shape)

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32).prefetch(2048)
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32).prefetch(2048)

    model = MyModel()

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)