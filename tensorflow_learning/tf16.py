
import tensorflow as tf
import numpy as np


SEED = 23455

rdm = np.random.RandomState(seed=SEED)
x = rdm.rand(32,2)#32个样本，每个样本用两个特征表示

#rdm.rand() / 10.0 - 0.05 加上随机噪声
y_ = [[x1 + x2 + (rdm.rand() / 10.0 - 0.05)] for (x1,x2) in x]

x = tf.cast(x,dtype=tf.float32)

#权重参数
w1 = tf.Variable(tf.random.normal([2,1],stddev=1,seed=1))
COST = 99
PROFIT = 1
epochs = 100
lr = 0.002
for epoch in range(epochs):
    with tf.GradientTape() as tape:
        #前向传播，计算预测值
        y = tf.matmul(x,w1)
        #自定义损失
        loss = tf.reduce_mean(tf.where(tf.greater(y,y_),(y - y_)*COST,(y_ - y) * PROFIT))
        
    grads = tape.gradient(loss,w1)
    w1.assign_sub(lr * grads)
    
    if epoch % 10 == 0:
        print("after %d training steps,w1 is"%(epoch))
        print(w1.numpy(),"\n")
print("final w1 is : ",w1.numpy())
        