#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import os,sys
def abpath():
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
abpath()