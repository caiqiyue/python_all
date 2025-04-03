
import tensorflow as tf


#生成正态分布
a = tf.random.normal([2,2])
b = tf.random.truncated_normal([2,2])#而且这些元素都在两倍标准差内，相对更集中

print(a)
print(b)

print("==================================================")

#在 [minval,maxval)左闭右开的区间内，生成均匀分布
c = tf.random.uniform([2,2],minval=1,maxval=10)
print(c)

print("=====================================")

x1 = tf.constant([[1.0,2.0],[3.0,4.0]],dtype=tf.float32)
print(x1)
x2 = tf.cast(x1,dtype=tf.int64)#强制类型转换，将float转为int
print(x2)

print(tf.reduce_max(x2))#找出张量中的最大值
print(tf.reduce_min(x2))#找出张量中的最小值
print(tf.reduce_sum(x2))#求张量的总和
print(tf.reduce_mean(x2,axis=0))#纵向求均值