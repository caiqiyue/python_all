"""
独热编码
将前向传播的结果，转为概率
"""

import tensorflow as tf

classes = 3
labels = tf.constant([1,0,2])
output = tf.one_hot(labels,depth=classes)
print(output)

y = tf.constant([1.01,2.01,-0.66])
y_pro = tf.nn.softmax(y)
print(y_pro)