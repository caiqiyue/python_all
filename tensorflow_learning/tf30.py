

import tensorflow as tf

import tf_keras

fashion = tf_keras.datasets.fashion_mnist
(x_train,y_train),(x_test,y_test) = fashion.load_data()

x_train,x_test = x_train/255.0,x_test/255.0

model = tf_keras.Sequential([
    tf_keras.layers.Flatten(),
    tf_keras.layers.Dense(128,activation='relu'),
    tf_keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
              loss = tf_keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics = ['sparse_categorical_accuracy']
              )

model.fit(x_train,y_train,batch_size=32,epochs=1,validation_data=(x_test,y_test),validation_freq=1)

model.summary()