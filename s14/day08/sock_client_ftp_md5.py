#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket,hashlib,os
client=socket.socket()
client.connect(("localhost",9999))
while True:
    cmd=input(">>:").strip()
    if len(cmd)==0:continue
    if cmd.startswith("get"):
        client.send(cmd.encode())  #1.发命令
        file_size=client.recv(1024)  #2.收文件大小\
        if file_size==b"00":
            print("没有该文件！请重新输入。。。")
            continue
        print("file size:",file_size.decode()) #打印文件大小
        file_total_size=int(file_size.decode())
        client.send(b"ready to recv file")  #3. 发  --准备好收文件
        received_size=0
        filename=cmd.split()[1]
        f=open(filename+".new","wb")
        m=hashlib.md5()
        while received_size<file_total_size:
            if file_total_size-received_size>=1024:
                size=1024
            else:
                size=file_total_size-received_size
            data=client.recv(size)
            received_size+=len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5=m.hexdigest()
            print("file recv done")
            f.close()
            server_file_md5=client.recv(1024)
            print("new_file_md5: ",new_file_md5)
            print("server_file_md5: ",server_file_md5.decode("GBK"))

            print("file_total_size: %s,   received_size: %s" % (file_total_size, received_size))
    else:
        print("命令输入错误！")
client.close()



