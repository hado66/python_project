#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import numpy as np
def bibao(a1,a2):
    m=int(a1.size**0.5)
    b = np.ones((m,m))
    for j in range(m):
        for i in range(m):
            min_que=np.minimum(a1[j,:],a2[:,i])
            b[j,i]=min_que.max()
    print(b)
    return b
a = np.array([[1,0.6,0.5,0.7,0],[0.4,1,0.7,0.9,0.2],[0.6,0.6,1,0.5,0],[0.5,0.7,0.9,1,0.6],[0.8,0,0.7,0.9,1]])
# a = np.array([[0.3,1.0],[0.8,0.1]])
# a = np.array([[0.9,0.5,0.3],[0.2,0.4,0.95],[0.8,0.1,0.25]])
# a=np.array([[1,0.3,0.1,0.4,0.8,0.7,0.6],[0.3,1,0.5,0.9,0.6,0.8,0.9],[0.1,0.5,1,0.7,0.6,0.2,0.1],[0.4,0.9,0.7,1,0.5,0.9,0.4],[0.8,0.6,0.6,0.5,1,0.7,0.5],[0.7,0.8,0.5,0.9,0.7,1,0.4],[0.6,0.9,0.1,0.4,0.5,0.4,1]])
print('R: ')
print(a)
print("\nR^2: ")
a1=bibao(a,a)  #R^2
print("\nR^3")
a2=bibao(a1,a)  #R^3
print("\nR^4")
a3=bibao(a1,a1) #R^4
print("\n R^5")
a4=bibao(a3,a)  #R^5