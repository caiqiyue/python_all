
import tensorflow as tf
import numpy as np


#交叉商损失函数
loss_ce1 = tf.losses.categorical_crossentropy([1, 0], [0.6, 0.4])
loss_ce2 = tf.losses.categorical_crossentropy([1, 0], [0.8, 0.2])
print("loss_ce1:", loss_ce1)
print("loss_ce2:", loss_ce2)

#softmax和交叉商结合
y_ = np.array([[1,0,0],[0,1,0],[0,0,1],[1,0,0],[0,1,0]])
y = np.array([[12,3,2],[3,10,1],[1,2,5],[4,6.5,1.2],[3,6,1]])

#先转成概率值
y_pro = tf.nn.softmax(y)
#才能使用交叉商
loss_ce1 = tf.losses.categorical_crossentropy(y,y_pro)
loss_ce2 = tf.losses.categorical_crossentropy(y_,y)

print(loss_ce1)
print(tf.nn.softmax_cross_entropy_with_logits(y,y_pro))#一步到位
print(loss_ce2)
print(tf.nn.softmax_cross_entropy_with_logits(y_,y))

