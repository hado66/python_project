#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket,os,hashlib,time
server=socket.socket()
#server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR) #断开连接后可以重用地址
server.bind(("localhost",9999))
server.listen()
while True:
    conn, addr = server.accept()
    print("new addr",addr)
    while True:
        print("等待新指令")
        data=conn.recv(1024)  # 1.收命令
        if not data:
            print("客户端已断开")
            break
        cmd,filename=data.decode().split()
        print("获取文件名",filename)
        if os.path.isfile(filename):
            f=open(filename,"rb")
            m=hashlib.md5()
            file_size=os.stat(filename).st_size
            conn.send(str(file_size).encode())# send file size   # 2.发文件大小
            print("file_size:",file_size)
            conn.recv(1024)#wait for ack  #3. 收到客户端已准备好---返回的消息
            for line in f:
                m.update(line)
                conn.send(line)
            print("md5",m.hexdigest())
            f.close()
            #time.sleep(0.5)   #粗略解决黏包  >>--在循环收的时候做判断，最后一次不足1024，就收应有的那些
            conn.send(m.hexdigest().encode())
            print("send done")
        else:
            conn.send(b"00")
server.close()
