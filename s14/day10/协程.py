#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import time

#遇到io操作，就切换
def home():
    print("in func home")
    time.sleep(5)#代表 get data from db
    print("home exec done")

def bbs():
    print("in func bbs")
    time.sleep(2)


def login():
    print("in func login")