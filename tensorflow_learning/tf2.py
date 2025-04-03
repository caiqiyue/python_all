import tensorflow as tf


w = tf.Variable(tf.constant(5,dtype=tf.float32))#初始化w值为5，并定义为可训练参数
lr = 0.2#学习率
epochs = 40#训练轮数
"""
TensorFlow 的 自动求导 机制，tf.GradientTape() 记录在 with 代码块内发生的所有计算，以便后续计算梯度
"""
for epoch in range(epochs):
    with tf.GradientTape() as tape:
        loss = tf.square(w + 1)#计算损失函数 （w + 1）** 2
    grads = tape.gradient(loss,w)#计算 loss 相对于 w 的梯度  2(w + 1)
    
    w.assign_sub(lr * grads)#相当于 w = w - lr*grads 进行梯度计算
    print("after %s epoch ,w is %f "%(epoch,w.numpy()),loss)