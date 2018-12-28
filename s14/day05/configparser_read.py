#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import configparser
conf=configparser.ConfigParser()
conf.read("example.ini")
print(conf.defaults())
print(conf["bitbucket.org"]["user"])
for i in (conf["DEFAULT"]):
    print(i)
