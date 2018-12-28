#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import threading
import time
def run(n):
    lock.acquire()
    global num
    num += 1
    time.sleep(0.001)
    lock.release()
lock=threading.Lock()
num=0
t_obj=[]#存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_obj.append(t)
for t in t_obj:
    t.join()
print("_____all threads has finished ---- ",threading.current_thread(),threading.active_count())
print("num :" , num)


