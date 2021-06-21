import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

EPOCHS = 100

def MyModel():
    feat = tf.keras.applications.MobileNetV2(intput_shape=(224, 224, 3),
                                             include_top=False)
    feat.trainable = False

    seq = tf.keras.models.Sequential()
    seq.add(feat)
    seq.add(tf.keras.layers.GlobalAveragePooling2D())
    seq.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    return seq

def preprocess(img, label):
    img = tf.cast(img, tf.float32) / 255.0
    img = tf.image.resize(img, (224, 224))
    return (img, label)

if __name__ == '__main__':
    train_ds, test_ds, meta = tfds.load(name='cats_vs_dogs',
                              split=('train[:80%]', 'test'),
                              with_info=True,
                              as_supervised=True)

    train_ds = train_ds.map(preprocess).batch(32).prefetch(1024)
    test_ds = test_ds.map(preprocess).batch(32).prefetch(1024)

    model = MyModel()
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)