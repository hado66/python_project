#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket
server=socket.socket()
server.bind(("localhost",8888))#绑定要监听的端口，
server.listen(5)#监听 5指最大允许的排队数
while True:
    conn,addr=server.accept()#等电话打进来
    print("连接成功")
    while True:
        data=conn.recv(1024) #接收
        print("recv:",data)
        if not data:
            print("client is lost ...")
            break
        # conn.send(data.upper())
server.close()
