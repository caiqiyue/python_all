

import tensorflow as tf
import tf_keras
from tf_keras.layers import Dense
from tf_keras import Model

from sklearn import datasets
import numpy as np

x_train = datasets.load_iris().data
y_train = datasets.load_iris().target`

np.random.seed(116)
np.random.shuffle(x_train)
np.random.seed(116)
np.random.shuffle(y_train)
tf.random.set_seed(116)


#自定义模型
class IrisModel(Model):
    def __init__(self):
        super(IrisModel,self).__init__()
        self.d1 = Dense(3,activation='sigmoid',kernel_regularizer=tf_keras.regularizers.l2())
        
        
    def call(self,x):
        y = self.d1(x)
        return y
    
model = IrisModel()

model.compile(optimizer=tf_keras.optimizers.SGD(lr=0.1),
              loss = tf_keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics = ['sparse_categorical_accuracy']
              )

model.fit(x_train,y_train,batch_size=32,epochs=500,validation_split=0.2,validation_freq=20)

model.summary()


`