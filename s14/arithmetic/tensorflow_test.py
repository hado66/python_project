#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

a=3
w=tf.Variable([[0.8,2.0]])
x=tf.Variable([[2.0],[1.0]])
y=tf.matmul(w,x)
init_op=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(y.eval())


print("-------------------------")
a=np.ones((3,3))
ta=tf.convert_to_tensor(a)
with tf.Session() as sess:
    print(sess.run(ta))


input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)
output=tf.multiply(input1,input2)
with tf.Session() as sess:
    print(sess.run([output],feed_dict={input1:[7.0],input2:[2.0]}))

print("-----------------------画图----------------")
num_points=1000
vectors_set=[]
for i in range(num_points):
    x1=np.random.normal(0.0,0.55)
    y1=x1*0.1+0.3+np.random.normal(0.0,0.03)
    vectors_set.append([x1,y1])
#生成一下样本
x_data=[v[0] for v in vectors_set]
y_data=[v[0] for v in vectors_set]
plt.scatter(x_data,y_data,c='r')
plt.show()

