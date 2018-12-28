#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data=self.request.recv(1024).strip()
                self.add=self.client_address[0]
                print(self.add)
                print(self.data)
                self.request.send(self.data.upper())
        except ConnectionResetError as e:
            print("客户端异常关闭")
if __name__=="__main__":
    ip,port="localhost",9999
    server=socketserver.ThreadingTCPServer(("localhost",9999),MyTCPHandler)
    server.serve_forever()