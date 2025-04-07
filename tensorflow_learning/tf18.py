import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#读取数据集 300，3
df = pd.read_csv(r'tensorflow_learning\data\dot.csv')
#300，2 样本特征
x_data = np.array(df[['x1','x2']])
#300，1 标签
y_data = np.array(df['y_c'])

#制作训练集
x_train = np.vstack(x_data).reshape(-1,2)
y_train = np.vstack(y_data).reshape(-1,1)

#制作每个样本点的颜色 标签为1 的 为 红色，反之为蓝色
Y_c = [['red' if y else 'blue'] for y in y_train]

#强制类型转换
x_train = tf.cast(x_train,tf.float32)
y_train = tf.cast(y_train,tf.float32)

#划分 批次
train_db = tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(32)


#构建神经网络
#300，2  x 2,11 +  11,1
w1 = tf.Variable(tf.random.normal([2,11]),dtype=tf.float32)
b1 = tf.Variable(tf.constant(0.01,shape = [11]))
#300,11  x  11,1 + 1,1
w2 = tf.Variable(tf.random.normal([11,1]),dtype=tf.float32)
b2 = tf.Variable(tf.constant(0.01,shape=[1]))

lr = 0.005
epoch = 500
#进行训练
for e in range(epoch):
    for step,(x_train,y_train) in enumerate(train_db):
        with tf.GradientTape() as tape:
            #进行前向传播
            h1 = tf.matmul(x_train,w1) + b1
            h1 = tf.nn.relu(h1)
            y = tf.matmul(h1,w2) + b2
            #均方误差
            loss = tf.reduce_mean(tf.square(y_train - y))
            
        variables = [w1,b1,w2,b2]
        #权重参数求导
        grads = tape.gradient(loss,variables)
        #更新
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])
        w2.assign_sub(lr * grads[2])
        b2.assign_sub(lr * grads[3])
        
    if e % 100 == 0:
        print("epoch",e,'loss:',float(loss))
        
print("predict================================")
#从-3 到 3 步长为 0.1 共60，60 个 作为 x轴，和 y轴的 左边
xx,yy = np.mgrid[-3:3:0.1,-3:3:0.1]
#x轴和y轴 坐标点 拉平 并 对应的点 合并 共 3600个坐标点
grid = np.c_[xx.ravel(),yy.ravel()]
grid = tf.cast(grid,tf.float32)
#记录预测值
probs = []

#对 坐标点进行 预测
for x_test in grid:
    #前向传播
    h1 = tf.matmul([x_test,],w1) + b1
    h1 = tf.nn.relu(h1)
    y = tf.matmul(h1,w2) + b2
    #每个坐标点，被预测为的类别
    probs.append(y)
#所有样本的第一个特征
x1 = x_data[:,0]
#第二个特征，构成x,y坐标轴
x2 = x_data[:,1]

#probs [tf.logits,tf.logits,..........] 3600个预测值  -----> 3600,1,1 ----> 60,60 每个网格点的类别概率
probs = np.array(probs).reshape(xx.shape)
plt.scatter(x1,x2,color=np.squeeze(Y_c))#画出散点图
plt.contour(xx,yy,probs,levels=[0.5])#等高线图xx,yy是网格图的坐标 probs代表每个网格点的类别概率，只画出概率为0.5的网格点
plt.show()    



