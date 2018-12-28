#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import random
print(random.random()) #随机0-1之间的浮点数
print(random.randint(1,20))
print(random.uniform(1,8))
item=[1,2,3,4,5,6,7,8,9]
random.shuffle(item)
print(item)
