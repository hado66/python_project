#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"

# 协程就是在单线程的情况下，实现多并发的效果
import time
import queue
def consumer(name):
    print("--->%s starting eating baozi ...."%name)
    while True:
        new_baozi=yield #
        print("[%s] is eating baozi %s"%(name,new_baozi))
def producer():
    r=con.__next__()
    r=con2.__next__()
    n=0
    while n<5:
        n+=1
        con.send(n) #
        con2.send(n)
        time.sleep(0.5)
        print("\033[32;1m[producer]\033[0m is making baozi %s " %n)


if  __name__=="__main__":
    con=consumer("c1")
    con2=consumer("c2")
    p=producer()