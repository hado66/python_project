#!/usr/bin/python
#-*- coding:utf-8 -*-
# author=ziyuanwang
import  numpy as np
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
b = np.ones((5,5))
# print(a(0,2)) #获得列数，返回 5
print(a[0:1])
print(a[1,:]) #截取第二行，第三、四列，返回 [8 9]

print(a[0,:]) #截取第二行,返回 [ 6  7  8  9 10]
print(a[:,1]) #列
print(np.maximum(a[1,:],a[0,:]))
b[1,1]=555
print(b)
print()