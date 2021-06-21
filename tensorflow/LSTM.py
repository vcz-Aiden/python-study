import tensorflow as tf

EPOCHS = 10
NUM_WORDS = 10000

class MyMode(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.emb = tf.keras.layers.Embedding(NUM_WORDS, 16)
        #self.lstm = tf.keras.layers.LSTM(32)
        #self.gru = tf.keras.layers.GRU(32)
        self.rnn = tf.keras.layers.SimpleRNN(32)
        self.dense = tf.keras.layers.Dense(1, activation='sigmoid')

    def __call__(self, x, training=None, mask=None):
        x = self.emb(x)
        x = self.rnn(x)
        return self.dense(x)

if __name__ == '__main__':
    imdb = tf.keras.datasets.imdb
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=NUM_WORDS)

    x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train,
                                                            value=0,
                                                            padding='pre',
                                                            maxlen=32)

    x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test,
                                                            value=0,
                                                            padding='pre',
                                                            maxlen=32)

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(1000).batch(32)
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

    model = MyMode()
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)