#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from  multiprocessing import Process,Pool,freeze_support
import time,os
def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i+100
def Bar(arg):
    print("-->>exec done",arg,os.getpid())

if __name__=="__main__": #为了区分主动执行这个脚本，还是从别的模块导入
    # freeze_support()
    pool=Pool(processes=5) #允许进程池里同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        # pool.apply(func=Foo,args=(i,))#串行
        # pool.apply_async(func=Foo,args=(i,))  #串行
        pool.apply_async(func=Foo,args=(i,),callback=Bar) #callback=回调
    print("end")
    pool.close()   # 一定个要先关闭进程池再join，自己试试区别
    pool.join()#进程池中进程执行完毕后在关闭，如果注释，那程序直接关闭