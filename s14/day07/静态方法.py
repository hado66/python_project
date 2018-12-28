#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  os

class Dog(object):
    name="xuliangwei"
    def __init__(self,name):
        self.name=name
        self.__food=None

    #@staticmethod    #实际是跟类没什么关系了,名誉上归类管
    #@classmethod     #  @classmethod----类方法，只能访问类变量，不能访问实例变量
    @property    #属性方法---不动产    调用属性  d.eat
    def eat(self):
        print("%s is eating %s" % (self.name,self.__food))

    @eat.setter  #修改
    def eat(self, food):
        print("set to food:",food)
        self.__food=food
    @eat.deleter   #删除
    def eat(self):
        del self.__food
        print("删完了")

    def __call__(self, *args, **kwargs):
        print("running call",args,kwargs)

d=Dog("chengronghua")()

# d.eat(d) #调用时把实例本身传进去
# d.eat("baozi")
# d.eat
# d.eat="baozizizi"
# d.eat
# del d.eat
# d(3,3,6,7,8,9,9,0,0,name=66,age=77)
print(Dog.__dict__)



