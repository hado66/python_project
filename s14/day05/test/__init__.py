#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import os,sys
#import 包名，==运行__init.py__ __>
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
sys.path.append(path)
#
print(path)
#import test2   #结果将test2=“test2.py all code”.test2
import test2.test3


from test2.test3 import test3_son  #多层包的调用方法
test3_son
#test2
from test2 import test2_son  #调用同层包中的 .py文件

test2_son.sayhi()