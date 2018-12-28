#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
#class People():  #经典类

class People(object):  # 新式类
    def __init__(self,name,age):
        self.Name=name  #Name变量名，name参数名
        self.Age=age
        self.friends=[]
    def eat(self):
        print("%s is eating ...."%self.Name)
    def take(self):
        print("%s is taking ...."%self.Name)
    def sleep(self):
        print("%s is sleeping ..."% self.Name)

class Ralation(object):
    # def __init__(self):
    #     print(self.Name)
    def make_friends(self,obj):
        print("%s is making friends with %s"%(self.Name,obj.Name))
        self.friends.append(obj)

class Man(People,Ralation):
    # def __init__(self,name,age,money):
    #     #People.__init__(self,name,age)
    #     super(Man,self).__init__(name,age)   #新式类
    #     self.Money=money
    #     print("%s 一出生就有%s "%(name,self.Money))
    def piao(self):
        print("%s is piaoing..... 20s....done"% self.Name)
    def sleep(self):
        People.sleep(self)
        print("Man is sleeping ...")
class Woman(People,Ralation):
    def get_birth(self):
        print("%s is born a baby...."%self.Name)

w1=Woman("chen rong hua","22")
m1=Man("niu hai yang","22")

# m1.eat()
# m1.piao()
# m1.sleep()
# w1.get_birth()
w1.make_friends(m1)
#m1.Name="chan san pao "
print(w1.friends[0].Name)