#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import shelve
# f=shelve.open("test")
# info={"age":33,"job":'it'}
# name=["alex","test","aaaa"]
# f["name"]=name
# f["info"]=info
# f.close()
d=shelve.open("test")
print(d.get("name"))
print(d.get("info"))