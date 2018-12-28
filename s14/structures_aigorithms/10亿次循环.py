#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import time
start_time=time.time()
for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            # if (a**2+b**2+c**2==c**2 and a+b+c==100):
            if (a + b + c == 1000):
                if(a**2+b**2==c**2):
                     print("a,b,c :", a,b,c)
print("complete")
print("total_time",time.time()-start_time)
