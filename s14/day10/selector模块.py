#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import selectors
import  socket
sel =selectors.DefaultSelector()

def accept(sock,mask):
    conn,addr=sock.accept()
    print("accepted",conn,"from",addr,mask)
    conn.setblocking(False)  #非阻塞模式
    sel.register(conn,selectors.EVENT_READ,read)  #新连接注册read回调函数

def read(conn,mask):
    data=conn.recv(1024)
    if data:
        print("echoing",repr(data),"to",conn)
        conn.send(data.upper())
    else:
        print("closing",conn)
        sel.unregister(conn)
        conn.close()

sock=socket.socket()
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(("localhost",9991))
sock.listen(100000)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept)
while True:
    events=sel.select()  #默认阻塞，有活动连接就返回活动的连接列表
    for key,mask in events:
        callback=key.data  #accept
        callback(key.fileobj,mask)  #key.fileobj=文件句柄