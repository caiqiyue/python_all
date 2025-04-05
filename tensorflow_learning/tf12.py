

import tensorflow as tf


a = tf.constant([1,2,3,1,1])
b = tf.constant([0,1,3,4,5])

c = tf.where(tf.greater(a,b),a,b)
print(c) 
"""
greater 函数 以此比较 每个元素，如果大于则为 true ，true就返回a，false返回b

1 > 0 返回 1
2 > 1 返回 2
......
"""

print("=====================================================")

import numpy as np

rdm = np.random.RandomState(seed=1)#seed = 常数，每次生成随机数相同
g = rdm.rand()#返回一个随机标量 [0,1）之间的
h = rdm.rand(2,3)#返回 2行3列的随机数矩阵
print(g)
print(h)

print("============================================")

l = np.array([1,2,3])
k = np.array([4,5,6])
print(np.vstack((l,k)))
