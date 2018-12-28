#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  os,sys
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
from lib.aaa import C


obj=C()
print(obj.__module__)   #输出 lib.aa , 即：输出模块
print(obj.__class__)    #输出lib.aa.C, 即输出类