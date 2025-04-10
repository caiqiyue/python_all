import tensorflow as tf


import tf_keras

#读取手写数字 数据 训练集 60000  测试集 10000
mnist = tf_keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()

#数据归一化
x_train,x_test = x_train/255.0,x_test/255.0

#构建网络
model = tf_keras.models.Sequential([
    tf_keras.layers.Flatten(),#将28x28 ---> 784
    tf_keras.layers.Dense(128,activation='relu'),#784x128 + relu
    tf_keras.layers.Dense(10,activation='softmax')#128x10 + softmax
])


#模型训练配置
model.compile(optimizer='adam',
              #因为最后一层的输出已经使用softmax变为概率分布了，所以from_logits为False，如果输出不是 概率分布，就要True
              loss = tf_keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics = ['sparse_categorical_accuracy']#标签不是概率分布，是标签值（0-9），所以用 sparse
              )

#这里不用validation_split，直接填入测试集
model.fit(x_train,y_train,batch_size=32,epochs=5,validation_data=(x_test,y_test),validation_freq=1)

#打印模型 参数
model.summary()
