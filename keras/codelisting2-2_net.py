#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import os
from keras import models
from keras import layers
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
network=models.Sequential()
network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10,activation="softmax"))
x=np.array([[1],[3]])
print(x.shape())
past_velocity=0
momentum=0.1
loss=0
while loss>0.01:
    w,loss,gradient=get_c

