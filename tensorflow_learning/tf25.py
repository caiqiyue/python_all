

import tensorflow as tf
import tf_keras

from sklearn import datasets

import numpy as np

#150,4 150个样本，每个样本4维特征
x_train = datasets.load_iris().data
y_train = datasets.load_iris().target

np.random.seed(116)
np.random.shuffle(x_train)
np.random.seed(116)
np.random.shuffle(y_train)
tf.random.set_seed(116)

"""
Flatten() 拉直层，把特征变为一维特征
Conv2D 卷积层
LSTM()层
"""



model = tf_keras.models.Sequential([
    #3是神经元个数，Dense是全连接层，4x3 最后输出分类结果 因为鸢尾花有3个类别
    tf_keras.layers.Dense(3,activation='softmax',kernel_regularizer=tf_keras.regularizers.l2())
])
#优化器、损失函数、准确率

"""
SparseCategoricalCrossentropy  y_ = 0/1/2  y =[...,...,..]概率分布
CategoricalCrossentropy  y_  和 y都是概率分布
"""


model.compile(optimizer=tf_keras.optimizers.SGD(lr=0.1),
              loss = tf_keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy']
              )


#在fit中定义，测试集的比例
model.fit(x_train,y_train,batch_size=32,epochs=500,validation_split=0.2,validation_freq=20)

#打印整个网络的信息
model.summary()


