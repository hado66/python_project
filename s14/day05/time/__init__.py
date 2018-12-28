#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
# import time, datetime
# t=time.time()
# print(time.time())    ##  时间戳-->>从一九七零年开始
# print(time.localtime())
# print(time.gmtime())
# x=time.localtime()  #不带参数就获取现在， 带参数就是参数的时间
#
# print(x.tm_year)     #将数组转换为
# # print(help(x))
# print(x.tm_mon)
# print(time.mktime(x)) # 将数组转换为时间戳
# print("ddddd")
#
# time.strftime("%Y-%m-%d",x)
# print(x)

# print("------------")
# t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
# t = time.mktime(t)
# print(t)` -
# print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))
import time,datetime
print(time.time())
print(time.localtime())
x=time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",x))
print(datetime.datetime.now()+datetime.timedelta(hours=3))