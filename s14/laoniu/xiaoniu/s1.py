#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from django.shortcuts import HttpResponse
def index(request):
    return HttpResponse("我是 Python 大神")

def ssss(request):
    return HttpResponse("我ye是 Python 大神")