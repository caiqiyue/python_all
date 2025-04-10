

import tensorflow as tf

from matplotlib import pyplot as plt
import tf_keras

mnist = tf_keras.datasets.mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

plt.imshow(x_train[0],cmap='gray')

plt.show()

#每张图片28x28，训练集有60000
print(x_train[0])

print(y_train[0])

print(x_train.shape)

print(y_train.shape)
#测试集有 10000
print(x_test.shape)