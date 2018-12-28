#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket
client=socket.socket()#声明socket，同时生成socket连接对象
client.connect(("101.200.56.207",9997))
# client.connect(("localhost",8888))
while True:
    msg=input(">>:").strip()
    if len(msg)==0:
        continue
    client.send(msg.encode("utf-8"))
    data=client.recv(1024).decode()
    print(data)
client.close()