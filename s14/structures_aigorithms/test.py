#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
def fD(arr):
    if None==arr:
        return -1
    lens=len(arr)
    hT=dict()
    i=0
    while i<lens-1:
        hT[i]=0
        i+=1
        print(hT)
        print('i',i)
    j=0
    while j<lens:
        if hT[arr[j]-1]==0:
            hT[arr[j]-1]=arr[j]-1
            print('j',j)
        else:
            return arr[i]
            print('ddddiii',i)
        j+=1
    return -1
arr=[1,5,1,5,88,55,554,55,888]
a=fD(arr)
print(a)