#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import importlib
aaa=importlib.import_module("lib.aaa")
obj=aaa.C()
try:
    assert type(obj.name) is str #断言obj.name是str的类型，若是打印dddd；不是则执行 except 语句
    print("ddddd")
except AssertionError as e:
    print("bushizifuchuan")

