# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__="Ziyuan Wang"
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import captcha.image as ImageCaptcha
state = tf.Variable(0)  # 定义变量
new_value = tf.add(state, tf.constant(1))  # 加一
update = tf.assign(state, new_value)  # 赋值
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(state))
    for i in range(5):
        sess.run(update)
        print(sess.run(state))

"""numpy转换为tensor"""
a = np.zeros((4, 4))
ta = tf.convert_to_tensor(a)
with tf.Session() as sess:
    print(sess.run(ta))

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1: [7.], input2: [2.]}))

"""线性回归模型"""
num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 5.5)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

# 生成一些样本
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]
plt.scatter(x_data, y_data, c='r')
plt.show()
# 生成1维的W矩阵，取值是[-1,1]之间的随机数
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
b=tf.Variable(tf.zeros([1],name="b"))
# 经历计算得出预估值y
y = W * x_data + b
# 以预估值y和实际值y_data之间的均方误差作为损失
loss = tf.reduce_mean(tf.square(y - y_data), name='loss')
# 采用梯度下降法来优化参数
optimizer = tf.train.GradientDescentOptimizer(0.5) #0.5代表学习率
train = optimizer.minimize(loss, name="train")
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# 初始化的W和b是多少
print("W=", sess.run(W), "b=", sess.run(b), "loss=", sess.run(loss))
# 执行20次训练
for step in range(20):
    sess.run(train)
    # 输出训练好的W和b
    print("W=", sess.run(W), "b=", sess.run(b), "loss=", sess.run(loss))


from keras.datasets import mnist
from keras import models
from  keras import layers
network=models.Sequential()
network.add(layers.Dense(512,activation="relu",input_shape=(28*28,)))
network.add(layers.Dense(512,activation="softmax"))

network.compile(optimizer="rmsprop",
                loss="categorical_crossentropy",
                metrics=['accuracy'])

sess=tf.Session()
sess.run()
sess.close()

import tensorflow as tf
matrix1=tf.constant([3,3])
matrix2=tf.constant([[2],[3]])
product=tf.matmul(matrix1,matrix2)

sess.Session()
result=sess.run(product)
print(result)










