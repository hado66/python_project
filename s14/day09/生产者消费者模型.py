#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  queue,threading,time

q=queue.Queue(maxsize=10)
def Producer(name):
    count=0
    while True:
        q.put("骨头 %s"%count)
        time.sleep(2)
        print("生产了",count)
        count+=1
def Consumer(name):
    # while q.qsize()>0:
    while True:
        print("[%s]取到[%s]并吃了它 。。。 "%(name,q.get()))
        time.sleep(0.5)
p=threading.Thread(target=Producer,args=("alex",))
c=threading.Thread(target=Consumer,args=("chenronghua",))
c1=threading.Thread(target=Consumer,args=("王森",))

p.start()
c.start()
c1.start()