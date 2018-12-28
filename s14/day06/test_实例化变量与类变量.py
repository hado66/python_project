#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
class Person:
    cn = "中国" #节省开销
    name="ziyuan"

    def __init__(self, name, age, addr):
        self.name = name
        self.age=age
        self.addr=addr
        print("this is __init__")
    def __del__(self,dead_name):
        print("%s 彻底死了。。。。。" % dead_name)
    def test(self,test_name):
        print("this is test,%s" % test_name)


p1 = Person("name", "age", "addr")
# p2 = Person("name", "age", "addr")
# p3 = Person("name", "age", "addr")
# print(p1.name)
# print(p1.cn)
# p1.cn="japan"
# Person.cn="us"
# print(p1.cn)
# print(p2.cn)
# print(p3.cn)
# print("person.name",Person.name)