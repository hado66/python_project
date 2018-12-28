#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
names=["alex","jack"]
data={}
a=1
try:
    # names[3]
    # data["ddd"]
    print(a)
except IndexError as e:
    print("列表操作错误",e)
except KeyError as e:
# except Exception as e: 抓住所有的错误
    print("没有这个",e)
else:
    print("一切正常")
finally:
    print("不用有没有错，就不执行")