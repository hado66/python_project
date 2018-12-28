# !/usr/bin/python
# -*- coding: UTF-8 -*-
# __author__ = "Ziyuan Wang"
import json,codecs,pickle
def sayhi(name):
    print("hello2,",name)

f=open("text.txt","rb")   #读
data=pickle.load(f)        #data = pickle.loads(f.read())
print(data["func"]("alex"))



