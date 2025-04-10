

import tensorflow as tf

from tf_keras.layers import Flatten,Dense

from tf_keras import Model

import tf_keras


fashion = tf_keras.datasets.fashion_mnist

(x_train,y_train),(x_test,y_test) = fashion.load_data()

class FashionClass(Model):
    def __init__(self):
        super(FashionClass,self).__init__()
        self.flat = Flatten()
        self.d1 = Dense(128,activation='relu')
        self.d2 = Dense(10,activation='softmax')
        
    def call(self,x):
        x = self.flat(x)
        x = self.d1(x)
        y = self.d2(x)
        return y
    
    
model = FashionClass()

model.compile(optimizer=tf_keras.losses.SGD(lr = 0.1),
              loss = tf_keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics = ['sparse_categorical_accuracy'])

model.fit(x_train,y_train,batch_size=32,epochs=1,validation_data=(x_test,y_test),validation_freq=1)

model.summary()

