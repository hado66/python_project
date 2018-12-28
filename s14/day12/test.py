#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import random,string
print(random.choice("asgasdgas"))
salt = ''.join(random.sample(string.ascii_letters + string.digits+"!@#$%^&*()_+", 6))
print (salt)