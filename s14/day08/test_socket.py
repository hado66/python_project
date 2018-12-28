#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from http.server import HTTPServer,CGIHTTPRequestHandler
port=8080
httpd=HTTPServer(("",port),CGIHTTPRequestHandler)
print("欢迎  端口号"+str(httpd.server_port))
httpd.serve_forever()