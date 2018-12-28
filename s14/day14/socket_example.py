#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket
import time

def handle_request(client):
    buf=client.recv(1024)
    client.send(b"HTTP/1.1 200 OK\\r\n\r\n")
    f=open("index.html","r",encoding="utf-8")
    data=f.read()
    f.close()
    a=get_time()
    data=data.replace("@@@",a)
    client.send(data.encode("utf-8"))

def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("localhost",8000))
    sock.listen(5)
    while True:
        conn,addr=sock.accept()
        handle_request(conn)
        conn.close()
def get_time():
    a=int(time.time())
    a=time.localtime(a)
    a=time.strftime('%Y-%m-%d %H:%M:%S',a)
    return a
if __name__=="__main__":
    main()