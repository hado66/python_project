#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import os,sys
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main
from conf import setting
from a import a

main.login()



