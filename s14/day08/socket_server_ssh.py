#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket,os,time
server=socket.socket()
server.bind(("localhost",9997))
server.listen()
while True:
    conn, addr = server.accept()
    print("new conn",addr)
    while True:
        data=conn.recv(1024)
        if not data:
            print("客户端断开")
            break
        print("执行指令",data)
        cmd_res=os.popen(data.decode()).read() #接收字符串，执行结果也是字符串
        if len(cmd_res)==0:
            cmd_res="This cmd has no output...."
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))  #先将文件的大小发给客户端
        # time.sleep(0.5)
        client_ack=conn.recv(1024)# wait client to confirm
        conn.send(cmd_res.encode("utf-8"))
server.close()