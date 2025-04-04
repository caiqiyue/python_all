"""
gradienttape实现，某个函数对某个参数的求导运算
with tf.GradientTape as tape:
    若干计算过程

grad = tape.gradient(函数,对谁求导)
"""

import tensorflow as tf

with tf.GradientTape() as tape:
    w = tf.Variable(tf.constant(3.0))
    loss = tf.pow(w,2)#损失函数

grad = tape.gradient(loss,w)#损失函数对参数w求导
print(grad)