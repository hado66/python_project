#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import multiprocessing
def f(l,i):
    l.acquire()
    try:
        print("hello world",i)
    finally:
        l.release()
if __name__=="__main__":
    lock=multiprocessing.Lock()
    for num in range(10):
        multiprocessing.Process(target=f,args=(lock,num)).start()