import tensorflow as tf
import numpy as np


a = tf.constant([1,5],dtype=tf.int64)#创建一维向量
print(a)
print(a.shape)#打印形状
print(a.dtype)#打印数据类型

print("=================================================")

n = np.arange(0,5)
n_to_tf = tf.convert_to_tensor(n,dtype=tf.int64)#将numpy转为tensor

print(n)
print(n_to_tf)

print("=================================================")


zeros = tf.zeros([2,3])#创建2行3列的全为0的矩阵
ones = tf.ones(4)#创建4维向量，全为1
nine = tf.fill([2,2],9)#创建一个2行2列的矩阵，全部填充为9
print(zeros)
print(ones)
print(nine)