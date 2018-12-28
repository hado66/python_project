#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
class Dog():
    def __init__(self,name):
        self.name=name
    def eat(self,food):
       print("%s is eating ...%s"%(self.name,food))
    def sleep(self):
        print("%s is sleeping ..."%(self.name))
def bulk(self):
    print("%s is bulk"%self.name)
d=Dog("niu hang yang")
choice=input(">>:").strip()
print(type(choice))
choice_result=hasattr(d,choice)
if choice_result==True:
    # # func=getattr(d,choice)    #getattr(d,choice)<->是个内存地址
    # # func()
    # attr=getattr(d,choice)
    # setattr(d,choice,"ronghua")
    delattr(d,choice)

else:
    # setattr(d,choice,bulk) #将外面的方法装载进 类中
    # d.talk(d)

    setattr(d,choice,22) # 设置静态属性
    print(getattr(d,choice))

print(d.name)