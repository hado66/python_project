#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
print('\n'.join([''.join([('❤❤❤'[(x-y) % len("❤❤❤")] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

# print('\n'.join([''.join([("❤"[(x-y) %len("❤")] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
print(len("❤"))