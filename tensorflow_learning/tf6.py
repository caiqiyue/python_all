import tensorflow as tf


features = tf.constant([10,27,21,19])
labels = tf.constant([0,1,1,0])
#将特征和标签配对，组成（特征，标签），（特征，标签）
dataset = tf.data.Dataset.from_tensor_slices((features,labels))
print(dataset)

for data in dataset:
    print(data)