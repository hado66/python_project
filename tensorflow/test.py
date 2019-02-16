#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import tensorflow as tf
print(tf.__version__)
w=tf.Variable([[0.5,1.0]]) #创建行向量
x=tf.Variable([[2.0],[1.0]])#定义列向量
y=tf.matmul(w,x)#定义矩阵相乘

a=tf.zeros([3,4])
tensor=tf.constant([[1,2,3],[4,5,6]]) #定义矩阵
b=tf.ones_like(tensor)



norm=tf.random_normal([2,2],mean=0,stddev=1)#mean均值，stddev标准差
init_op=tf.global_variables_initializer()#对全局变量进行初始化
with tf.Session() as sess:
    sess.run(init_op)
    print(y.eval())
    print(a.eval())
    print(tensor.eval())
    print(b.eval())
    print(norm.eval())

# print(a)