#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
class Alexexcept(Exception):
    def __init__(self,name):
        self.name=name
try:
    raise  Alexexcept("woshizidingyi")
except Alexexcept as e:
    print(e)


