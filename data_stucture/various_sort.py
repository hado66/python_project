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

def shell_sort(alist):
    """希尔排序"""
    n=len(alist) #n=21
    gap=4
    #gap变化到0之前，插入算法执行的次数
    while gap>=1:
        #shell排序，与普通查重排序的区别就是设置步长
        for j in range(gap,n): #处理一种gap的情况
            #j=[gap,gap+1,gap+2,gap+3,...,n-1]
            i=j
            while i>0:
                if alist[i-gap]>alist[i]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=gap
                else:
                    break
        gap=gap//2
    return alist

def quick_sort(alist,first,last):
    """快速排序"""
    if first>=last:
        return alist
    n=len(alist)
    mid_value=alist[first]
    low=first
    high=last
    while low<high:
        while low <high and alist[high]>=mid_value:
            #high左移动
            high-=1
        alist[low]=alist[high]
        while low<high and [low]<mid_value:
            #low右移动
            low+=1
        alist[high]=alist[low]
    alist[low]=mid_value
    #对low左边元素进行快速排序
    quick_sort(alist,first,low-1)
    #对low右边的元素进行快速排序
    quick_sort(alist,low+1,last)
    return alist

def merge_sort(alist):
    """归并排序"""
    n=len(alist)
    if n<=1:
        return alist
    mid=n//2
    left_li=merge_sort(alist[:mid])  #将整个链表的元素分开
    right_li=merge_sort(alist[mid:])
    left_pointer,right_pointer=0,0   #定义两个指针
    result=[]
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer]<=right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_pointer])
            right_pointer+=1
    result+=left_li[left_pointer:]
    result+=right_li[right_pointer:]
    print(alist)
    return result





if __name__=="__main__":
    # alist=[881,20,35,4,15,8,7,454,55,55,2,1,33,33,45,87,9,65,559,656,6698,225]
    alist=[10,3,3,1,55]
    print(alist)
    a=merge_sort(alist)
    print(a)



