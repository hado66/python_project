#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket
import sys
messages=[b"This is the message.",
          b"It will be sent",
          b"in parts.",]
server_address=("140.143.25.160",9991)

socks=[socket.socket(socket.AF_INET,socket.SOCK_STREAM) for  i in range(5000)
       ]
print(socks)

print("connecting to %s port "%str(server_address))
for s in socks:
    s.connect(server_address)
for message in messages:

    for s in socks:
        print("%s sending  %s"%(s.getsockname(),message))
        s.send(message)
    for s in socks:
        data=s.recv(1024)
        print("%s: received %s"%(s.getsockname(),data))
        if not data:
            print("closing socket",s.getsockname())