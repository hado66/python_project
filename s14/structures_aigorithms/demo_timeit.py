#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import timeit
def test1():
    li=[]
    for i in range(10000):
        li.append(i)

def test2():
    li=[]
    for i in range(10000):
        li+=[i]  #过程，，本来有俩个列表，然后合并

def test3():
    li=[i for i in range(10000)]
def test4():
    li=list(range(10000))
def test5():
    li=[]
    for i in range(10000):
        li.extend([i])

timer1=timeit.Timer("test1()","from __main__ import test1")
print("append",timer1.timeit(1000))
timer2=timeit.Timer("test2()","from __main__ import test2")
timer3=timeit.Timer("test3()","from __main__ import test3")
timer4=timeit.Timer("test4()","from __main__ import test4")
print("+:",timer2.timeit(1000))
print("[i for i in range]",timer3.timeit(1000))
print("list(range())",timer4.timeit(1000))
timer5=timeit.Timer("test5()","from __main__ import test5")
print("extend:",timer5.timeit(1000))
