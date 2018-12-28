#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all() #把当前程序的所有io操作给我单独的坐上标记

def f(url):
    print("GET:%s"%url)
    resp=request.urlopen(url)
    data=resp.read()
    print("%d bytes received from %s \n"%(len(data),url))
urls=["https://www.cnblogs.com/alex3714/category/770733.html",
      "https://vip.iqiyi.com/waimeizhy1-pc.html",
      "https://www.zhihu.com/signup?next=%2F"]
time_start=time.time()
for url in urls:
    f(url)
print("同步cost%d \n",time.time()-time_start)
async_time=time.time()
gevent.joinall([
    gevent.spawn(f,"https://www.cnblogs.com/alex3714/category/770733.html"),
    gevent.spawn(f, "https://vip.iqiyi.com/waimeizhy1-pc.html"),
    gevent.spawn(f, "https://www.zhihu.com/signup?next=%2F"),
])
print("异步cost%d \n",time.time()-async_time)
