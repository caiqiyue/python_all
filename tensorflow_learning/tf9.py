"""
assign_sub： 相当于  -=
但是要求 自更新的 参数 是被标记为可训练的参数
"""


import tensorflow as tf


w = tf.Variable(4)
w.assign_sub(1)
print(w)

import numpy as np

test = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(test)
print(tf.argmax(test,axis=0))#返回最大值的索引
print(tf.argmax(test,axis=1))