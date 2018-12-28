#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"

import  socket
client=socket.socket()
port=22
# client.connect("dsag",port)
s="I love you "
s1,s2,s3=s.split()
print(type(s1))
print(s1)
print(s2)
print(s3)
print(s.split()[2])