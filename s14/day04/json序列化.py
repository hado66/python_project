#!/usr/bin/python
#-*- coding: UTF-8 -*-
__author__ = "Ziyuan Wang"
import json,codecs,pickle
def sayhi(name):
    print("hello",name)
info={
    "name":"alex",
    "age":22,
    "func":sayhi
}
# f=open("test.txt","w",encoding='utf-8')  # 写
# f.write(str(info))
#
# f.close()

# f=codecs.open("test.txt","w",encoding="utf-8")
# f.write(str(info))
# f.close()
f=open("test.txt","wb")
f.write(pickle.dumps(info))
f.close()