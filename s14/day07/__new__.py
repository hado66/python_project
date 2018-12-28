#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
# class Foo(object):    #普通方式
#     def __init__(self,name):
#         self.name=name
# f=Foo("alex")
# print(type(f))
# print(type(Foo))

#装逼方式
def func(self):
    print("hello wu pei qi %s"%(self.name))
def __init__(self,name,age):
    self.name=name
    self.age=age
Foo=type("Foo",(object,),{"talk":func,
                          "__init__":__init__
                          })   #Foo的对象
f=Foo("test_alex",22)
f.talk()
print(type(Foo))