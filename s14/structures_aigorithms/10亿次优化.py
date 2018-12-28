#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import time
start_time=time.time()
for a in range(1000):
    for b in range(1000):
         c=1000-a-b
         if  a**2+b**2==c**2:
             print("a,b,c :",a,b,c)
print("complete")
print("total_time",time.time()-start_time)
