# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from numpy.random import RandomState

# 定义训练数据batch的大小
batch_size = 8

# 定义神经网络的参数
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 训练集的输入数据和对应的标签
x = tf.placeholder(tf.float32, shape=(None,2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None,1), name='y-input')

# 定义神经网络前向传播的过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播的算法
cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
train_start = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 通过随机数生成一个模拟数据集
rdm = RandomState(1)        # 1为随机种子
dataset_size = 128
X = rdm.rand(dataset_size, 2)
# X = rdm.uniform(3, 4, (2, 3))
'''
X的输出结果
array([[3.26865012, 3.80827801, 3.29528879],
       [3.54412138, 3.48792149, 3.85535641]])
'''


Y = [[int(x1+x2 < 1)] for (x1, x2) in X]

init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(w1))
    print(sess.run(w2))
    '''
    在训练之前神经网络的参数的值:
    w1 = [[-0.8113182   1.4845988   0.06532937]
                [-2.4427042   0.0992484   0.5912243 ]]
    w2 = [[-0.8113182 ], [ 1.4845988 ], [ 0.06532937]]
    '''
    trainStep = 5000
    for i in range(trainStep):
        # 每次选取 batch_size 个样本进行训练。
        start = (i * batch_size) % dataset_size
        end = min(start+batch_size, dataset_size)

        # 通过选取的样本训练神经网络并更新参数
        sess.run(train_start, feed_dict={x: X[start: end], y_: Y[start: end]})
        if i % 1000 == 0:
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict= {x: X, y_: Y})
            print("After %d training step(s), cross entropy on all data is %g" %(i, total_cross_entropy))
            '''
            输出结果：
            After 0 training step(s), cross entropy on all data is 0.0674925
            After 1000 training step(s), cross entropy on all data is 0.0163385
            After 2000 training step(s), cross entropy on all data is 0.00907547
            After 3000 training step(s), cross entropy on all data is 0.00714436
            After 4000 training step(s), cross entropy on all data is 0.00578471
            '''
    print(sess.run(w1))
    print(sess.run(w2))
    '''
    在训练之后神经网络的参数的值：
    w1 = [[-1.9618274  2.582354   1.6820377]
             [-3.4681718  1.0698233  2.11789  ]]
    w2 = [[-1.8247149], [ 2.6854665], [ 1.418195 ]]
    '''
    print('版本号',tf.__version__)
    import  time
    t=time.time()
    print(t)
