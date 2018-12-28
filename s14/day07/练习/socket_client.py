#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  socket
client=socket.socket()
client.connect(("192.168.100.74",8080))
client.send(b"abcdef")
print(client.recv(1024))
client.close()