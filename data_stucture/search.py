#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
def binary_search(alist,item):
    """二分查找，递归"""
    n=len(alist)
    if n>0:
        mid=n//2
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    return False

def binary_search_non_recursion(alist,item):
    """二分法，非递归"""
    n=len(alist)
    first=0
    last=n-1
    while first <=last:
        mid = (first + last) // 2
        if alist[mid]==item:
            return True
        elif item<=alist[mid]:
            last=mid-1
        else:
            first=mid+1
    return False

if __name__ == '__main__':
    list=[17,20,25,36,69,98,1000]
    print(binary_search(list,20))
    print(binary_search_non_recursion(list,17))