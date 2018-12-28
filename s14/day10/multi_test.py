#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import threading,multiprocessing,time

def thead_run():
    print(threading.get_ident())
def run(name):
    time.sleep(0.5)
    print("name",name)
    t=threading.Thread(target=thead_run,)
    t.start()
if __name__=="__main__":
    for i in range(10):
        t=multiprocessing.Process(target=run,args=("wzy%s"%i,))
        t.start()
