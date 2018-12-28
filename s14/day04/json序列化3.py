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
f=open("test3.txt","w")
f.write(json.dumps(info))
info["age"]=21

f.write(json.dumps(info))

f.close()



