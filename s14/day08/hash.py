#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  hashlib
m=hashlib.md5()
m.update(b"asdgfsag")
print(m.hexdigest())