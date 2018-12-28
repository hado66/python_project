# !/usr/bin/python
# -*- coding: UTF-8 -*-
# __author__ = "Ziyuan Wang"
import json
def sayhi(name):
    print("hello,",name)

info={
    "name":"alex",
    "age":22,
   # "func":sayhi
}
#python 2.7中可以多次load，但是在3.0中只能一次，多次load也没有意义
f=open("test3.txt","r")
data=json.loads(f.read())
f.close()



