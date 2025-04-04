from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

#导入鸢尾花的 特征  和 标签
x_data = load_iris().data
y_target = load_iris().target

#打乱数据集
np.random.seed(116)#对数据集进行打乱，使用同样的随机种子，这样标签和数据集打乱后也是一一对应
np.random.shuffle(x_data)
#打乱标签
np.random.seed(116)
np.random.shuffle(y_target)

#划分训练集和测试集
tf.random.set_seed(116)
train_data = x_data[:-30]
train_label = y_target[:-30]
test_data = x_data[-30:]
test_label = y_target[-30:]

#强制转换训练集的数据类型
train_data = tf.cast(train_data,dtype=tf.float32)
test_data = tf.cast(test_data,dtype=tf.float32)

#特征和标签配对，形成 batch
train_db = tf.data.Dataset.from_tensor_slices((train_data,train_label)).batch(32)
test_db = tf.data.Dataset.from_tensor_slices((test_data,test_label)).batch(32)

#权重参数 和 偏置项
w1 = tf.Variable(tf.random.truncated_normal([4,3],stddev=0.1,seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3],stddev=0.1,seed=1))

#学习率
lr = 0.1
train_loss_results = []
test_acc = []
epochs = 500
loss_all = 0

for epoch in range(epochs):
    for step,(train_x,train_y) in enumerate(train_db):
        with tf.GradientTape() as tape:
            #前向传播
            y = tf.matmul(train_x,w1) + b1
            #将结果转换成概率
            y = tf.nn.softmax(y)
            #将标签转成独热编码
            y_ = tf.one_hot(train_y,depth=3)
            #均方误差
            loss = tf.reduce_mean(tf.square(y_ - y))
            #累加所有损失
            loss_all += loss.numpy()
        #计算梯度
        grads = tape.gradient(loss,[w1,b1])
        #更新参数
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])
    print("Epoch{e},loss{l}".format(e=epoch+1,l = loss_all / 4))
    train_loss_results.append(loss_all / 4)
    loss_all = 0
    total_correct,total_number = 0,0
    
    #使用测试集测试模型
    for test_x,test_y in test_db:
        #前向传播
        y = tf.matmul(test_x,w1) + b1
        #将结果转化为概率值
        y = tf.nn.softmax(y)
        #选取每一行中概率最大值的下标，即该样本的预测结果
        pred = tf.argmax(y,axis=1)
        #数据类型转换
        pred = tf.cast(pred,dtype=test_y.dtype)
        #预测结果和真实值进行比对，相同为1，不同为0
        correct = tf.cast(tf.equal(pred,test_y),dtype=tf.int32)
        #求和，即求有多少个相同的
        correct = tf.reduce_sum(correct)
        total_correct += int(correct)
        total_number += test_x.shape[0]
    acc = total_correct / total_number
    test_acc.append(acc)
    print("Test_acc",acc)
    print("--------------------------------")

#画图
plt.title('loss function Curve')
plt.xlabel("epoch")
plt.ylabel("loss")
plt.plot(train_loss_results,label = '$loss$')
plt.legend()
plt.show()

plt.title('Acc Curve')
plt.xlabel("epoch")
plt.ylabel('Acc')
plt.plot(test_acc,label = '$Accuracys$')
plt.legend()
plt.show()