# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 18:46:14 2018

@author: Administrator
"""
import tensorflow as tf
import numpy as np
a=np.ones((3,3))
ta=tf.convert_to_tensor(a)
with tf.Session() as sess:
    print(sess.run(ta))
    
input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)
output=tf.multiply(input1,input2)
with tf.Session() as sess:
    print(sess.run([output],feed_dict={input1:[7.],input2:[2.]}))