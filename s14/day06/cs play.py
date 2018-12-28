#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
class Role(object):
    n="123"
    name="123"  #类变量
    n_list=[]
    name="我是类变量"
    def __init__(self,name,role,weapon,life_value=10000,money=80000):
        #构造函数，
        #在实例化时，做一些实例的类的初始化的工作
        self.name=name  #实例变量，（静态属性，）作用域就是实例的本事
        self.role=role
        self.weapon=weapon
        self.__valuelife_value=life_value     #私有属性，私有方法和私有属性一致
        self.money=money
    def shot(self):  #类的方法
        print("shoting .....")
    def got_shot(self):  #类的方法，功能（动然属性）
        print("ah,I'm get shoted")
    def buy_weapon(self,gum_name):
        print("%s just bought %s" %(self.name,gum_name))
    def show_status(self):
        print("life_val:%s"%(self.__valuelife_value))
    def show_money(self):
        print("r1 money",self.money)
# r1=Role("alex","police","AK47")  # 把一个类变成一个具体对象的过程  ，实例化（初始化一个类，相当于造了一个对象）
# r1.shot()
# r2=Role("jake","terrorist","MK16")
# r2.buy_weapon("ak47")
# r5=Role("wangziyuan","police","m16K")

print(Role.n)
r1=Role("Alex","police","AK47")
r2=Role("Alex2","police2","MK16")
print(r1.name,r1.name)   #当类变量与实例化名字一样时，优先用 实例化中的变量
print("------")
r1.name="AlexAlex"
print("r1",r1.name)
r1.bullet_prove=True
print(r1.name,r1.bullet_prove)
print(r1.weapon)
del r1.weapon

r1.n="444444"
r1.n_list="from r1"
print(r1.n)
Role.n="ABC"
print(r1.n)
print(r2.n)
print(r1.n_list)
print(r2.n_list)
print(r1.money)
r1.show_money()

r1.show_status()


