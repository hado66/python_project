#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  select
import socket
import queue

server=socket.socket()
server.bind(("localhost",9991))
server.listen(10000)

server.setblocking(False)  #不阻塞
msg_dict={}

inputs=[server,]
#inputs=[server,conn]
outputs=[]
while True:
    readable,writeable,exceptional=select.select(inputs,outputs,inputs)
    print(readable,writeable,exceptional)
    for r in readable:
        if  r is server:  #代表来了一个新链接，
            conn,addr=server.accept()
            print("来了一个新链接",addr)
            inputs.append(conn)#是因为这个新建立的连接还没发数据过来，现在就接收的话程序就报错了，所以要想实现这个客户端发数据来时，
            #  server端能知道就需要让select再监测这个conn
            msg_dict[conn]=queue.Queue()#初始化一个队列，后面要存返回给客户端的这个数据
        else:
            data=conn.recv(1024)
            print("收到数据",data)
            msg_dict[r].put(data.upper())
            outputs.append(r) #放入返回的连接队列里
            # conn.send(data.upper())

    for w in writeable: #要返回给客户端的连接列表
        data_to_client=msg_dict[w].get()
        w.send(data_to_client)#返回给客户端原数据

        outputs.remove(w)#确保下次循环的时候writeable，不返回这个已经处理完的连接了
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dict[e]