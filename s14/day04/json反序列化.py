#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import json,pickle
# f=open("test.txt","r",encoding="utf-8") #传统
# print(f.read())
# f.close()
def sayhi(name):
    print("hello",name)
info={
    "name":"alex",
    "age":22,
    "addr":"河北省衡水市"
}

# f=open("test.txt","r",encoding="utf-8")    #读--老方法
# data=f.read()
# print(data)
# f.close()

# f=open("test.txt","r",encoding="utf-8")
# data=json.loads(f.read())
# print(data)

f=open("text.txt","rb")
data =pickle.loads(f.read())
print(data["func"]("alex"))