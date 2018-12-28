#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import redis
r=redis.Redis(host="127.0.0.1",port=6379,password="123456")
# r=redis.Redis(host="140.143.25.160",port=6379)

r.set(b'rrr',b'bb')
ff=r.get(b"aa")
print(str(ff).encode("utf-8"))