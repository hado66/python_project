# !/usr/bin/python
# -*- coding: UTF-8 -*-
# __author__ = "Ziyuan Wang"
import json,codecs,pickle
def sayhi(name):
    print("hello,",name)
info={
    "name":"alex",
    "age":22,
    'func':sayhi
}
f=open("text.txt","wb")  # 写
pickle.dump(info,f)    ##f.write( pickle.dumps( info) )
f.close()





