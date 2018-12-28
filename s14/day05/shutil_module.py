#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import shutil,sys,os

# f1=open("心灵鸡汤",encoding="utf-8")
# f2=open("心灵鸡汤_2","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2) # copy文件

shutil.copyfile("心灵鸡汤","心灵鸡汤9") #直接copy文件
print(os.listdir())
print(os.stat("note2")) #查看用户权限