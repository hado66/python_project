#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket
HOST="localhost"
PORT=9991
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    msg=bytes(input(">>"),encoding="utf-8")
    s.sendall(msg)
    data=s.recv(1024)
    print("Received",repr(data))  #repr 格式化输出
s.close()