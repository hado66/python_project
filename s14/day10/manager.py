#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import multiprocessing,os
def f(d,l):
    d[os.getpid()]=os.getpid()
    print("函数里字典",d)
    l.append(os.getpid())
    print("函数里列表",l)



if __name__=="__main__":
    with multiprocessing.Manager() as manager:
        d=manager.dict()

        l=manager.list(range(5))
        p_list=[]
        for i in range(10):
            p=multiprocessing.Process(target=f,args=(d,l))
            p.start()

        p_list.append(p)
        for res in p_list:#等待经常结束
            res.join()
        print("字典",d)
        print("列表",l)
