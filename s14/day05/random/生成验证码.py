#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import random
checkcode=''
# for i in range(4):   #生成数数字
#     current=random.randint(0,9)
#     checkcode+=str(current)
# print(checkcode)

for i in range(4):
    num=str(random.randint(0,9))
    alphabet_capital=chr(random.randint(65,90))
    alphabet_low=chr(random.randint(97,122))
    current=random.choice([num,alphabet_capital,alphabet_low])
    checkcode+=current
print(checkcode)

print(chr(79))
print(0)
print(chr(111))