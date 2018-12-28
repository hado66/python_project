#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):  # MyTCPHandler  继承socketserver.BaseRequestHandler
    def handle(self):  # 跟client所有的交互都是在handle完成的
        try:
            while True:
                self.data=self.request.recv(1024).strip()
                if not self.data:
                    break
                print("{} worte".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper()) #sendall是重复调用send
        except ConnectionResetError as e:
            print("客户端异常关闭")
if  __name__=="__main__":
    HOST,PORT="localhost",9999
    server=socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)# TCPServer负责监听等事项，，， 每一个请求过来，就会实例化一个MyTCPHandler类，\
    # 拿MyTCPHandler.handle与client进行交互
    #ThreadingTCPServer--多线程网络服务
    server.serve_forever()
"""
1.创建一个请求处理类，并且这个类继承BaseRequestHandler，并且还要重写父类里的handle
2.实例化TCPserver，并且传递 ip、port和上面创建的请求处理类 ，给到这个TCPserver

备注：
3.只处理一个请求
4.处理多个请求，永远执行
"""
