#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
class test(object):
    age=18
    def __init__(self,name,age=19):
        self.test_name=name
        self.age=age
    def show_name(self):
        print("this is show_name",self.test_name)
t1=test("wzy")
print(t1.test_name)
t1.show_name()
t1.age=90
print(t1.age)
