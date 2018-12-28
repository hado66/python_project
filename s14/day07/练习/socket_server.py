#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket
server=socket.socket()
server.bind(("192.168.100.74",8080))
server.listen()
conn,addr=server.accept()
print(conn.recv(1024))
conn.send(b"dsgasdagdshg")
server.close()
