#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang
import  socketserver,json,os,hashlib
class MySocketServer(socketserver.BaseRequestHandler):
    def put(self,*args):
        """接收客户端文件"""
        cmd_dic=args[0]
        filename=cmd_dic["filename"]
        filesize=cmd_dic["filesize"]
        # if os.path.isfile(filename):
        #     f=open(filename+".new","wb")
        # else:
        #     f=open(filename,"wb")
        f=open(filename+".new","wb")
        self.request.send("response".encode())
        received_size=0
        while received_size<filesize:
            data=self.request.recv(1024)
            f.write(data)
            received_size+=len(data)
        else:
            print("file [%s] has uploaded ..."%filename)
    def get(self,*args):
        """将本地(服务端)文件发送到客户端"""
        cmd_dic=args[0]
        filename=cmd_dic["filename"]
        if os.path.isfile(filename):
            self.request.send(b"file is exist")
            f = open(filename, "rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            self.request.send(str(file_size).encode())  # send file size   # 2.发文件大小
            print("file_size:", file_size)
            self.request.recv(1024)  # wait for ack  #3. 收到客户端已准备好---返回的消息
            for line in f:
                m.update(line)
                self.request.send(line)
            print("md5", m.hexdigest())
            f.close()
            # time.sleep(0.5)   #粗略解决黏包  >>--在循环收的时候做判断，最后一次不足1024，就收应有的那些
            self.request.send(m.hexdigest().encode())
            print("send done")
        else:
            self.request.send(b"00")
    def handle(self):
        try:
            print("{} is sending".format(self.client_address))
            while True:
                self.data=self.request.recv(1024).strip()
                #print("{} worte:".format(self.client_address[0]))
                print(self.data)
                cmd_dic=json.loads(self.data.decode())
                action=cmd_dic["action"]
                if hasattr(self,action):
                    func=getattr(self,action)
                    func(cmd_dic)
        except ConnectionResetError as e:
            print("客户端关闭")
if __name__=="__main__":
    ip,port="localhost",9999
    server=socketserver.ThreadingTCPServer((ip,port),MySocketServer)
    server.serve_forever()
