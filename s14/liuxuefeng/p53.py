#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import math
def ItenSimilarity(train):
    C=dict()
    N=dict()
    for u,items in train.items():
        for i in items:
            print(i)
            N[i]+=j
            for j in items:
                if i==j:
                    continue
                C[i][j]+=1
    W=dict()
    for i ,related_items in C.items():
        for j,cij in related_items.items():
            W[i][j]=cij/math.sqrt(N[i]*N[j])
    return W


A={"items":{"aa":"aaa","dd":"dsdfs"}}


ItenSimilarity(A)
