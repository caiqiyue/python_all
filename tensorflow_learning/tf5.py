import tensorflow as tf


"""
tf.Variable()会将变量标记为可训练，被标记的信息就会在反向传播的时候，记录梯度信息
tf.add tf.subtract,tf.multiply,tf.divide 四则运算要求张量大小相同,而且数据类型也需要一致
tf.square,tf.pow,tf.sqrt
tf.matmul 矩阵乘法

w = tf.Variable(tf.random.normal([2,2],mean=0,stddev=1))#初始化w的参数矩阵，同时标记为 可训练

"""

ones = tf.ones([1,4])
four = tf.fill([1,4],4.0)


print(ones)
print(four)

print(tf.add(ones,four))
print(tf.subtract(ones,four))
print(tf.multiply(ones,four))
print(tf.divide(ones,four))

print(tf.pow(four,3))
print(tf.square(four))
print(tf.sqrt(four))

print("=====================================")
a = tf.random.normal([3,2])
b = tf.random.normal([2,4])
c = tf.matmul(a,b)
print(c.shape)