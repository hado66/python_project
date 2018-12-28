#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
# mod=__import__("lib.aaa")
# obj=mod.aaa.C()
# print(obj.name)
import importlib
li=importlib.import_module("lib.aaa")
print(li.C().name)
