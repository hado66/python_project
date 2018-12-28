#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import multiprocessing    #multi --多  process---进程
import time,threading
def thread_run():
    print(threading.get_ident())
def run(name):
    time.sleep(2)
    print("hello",name)
    t=threading.Thread(target=thread_run,)
    t.start()
print(__name__)
if __name__=='__main__':
    for i in range(10):
        p=multiprocessing.Process(target=run,args=("alex%s"%i,))
        p.start()


    # p.join()
