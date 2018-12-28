#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import threading,time
event=threading.Event()
def lighter():
    count=0
    event.set()
    while True:
        if count>10 and count<20:
            event.clear() #清空标志位
            print("")
            print("\033[41;1mred light is on ... \033[0m")
        elif count>20:
            event.set()  #变 绿灯
            count = 0
        else:
            print("" )
            print("\033[42m green light is on ...\033[0m")
        time.sleep(0.5)
        count+=1
def car(name):
    while True:
        if event.is_set(): # 设置了标志位
            print("%s is running ...."%name)
            time.sleep(0.5)
        else:
            print( "waint .....")
            event.wait()
            
light=threading.Thread(target=lighter,)
light.start()
car1=threading.Thread(target=car,args=("baoshijie",))
car1.start()
