#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
def bubble_sort(alist):
    """冒泡排序"""
    n=len(alist)
    for j in range(0,n-1):
        count=0 #若本身是一个
        for i in range(0,n-1-j):
            #代表cur从头走到尾
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count+=1
        if count==0:
            break
    return alist

def elect_sort(alist):
    """选择排序"""
    n=len(alist)
    for j in range(n):
        #需要选择n-1次
        min_index = j
        for i in range(j,n):
            if alist[i]<alist[min_index]:
                min_index=i
        if j!=i:
            alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist

def insert_sort(alist):
    """插入排序""" #自造的 --有些计算冗余，因为找到该元素应有的位置，没毕业，在和前面的元素比较
    n=len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]
    return alist

def insert_sort_optimize(alist):
    """插入排序"""
    n=len(alist)
    for j in range(0,n):
        i=j
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i-=1
            else:
                break
    return alist


if __name__=="__main__":
    alist=[881,20,35,4,15,8,7]
    print(alist)
    print(insert_sort_optimize(alist))
    for i in range(9,11):
        print(i)
