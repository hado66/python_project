#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import socket,os,json,hashlib
class FtpClient(object):
    def __init__(self):
        self.client=socket.socket()
    def connection(self,ip,port):
       self.client.connect((ip,port))

    def interactive(self):
        while True:
            cmd=input(">>:").strip()
            if len(cmd)==0:continue
            cmd_str=cmd.split()[0]
            if hasattr(self,"cmd_%s"%cmd_str):
                func=getattr(self,"cmd_%s"%cmd_str)
                func(cmd)
            else:
                self.help()
    def help(self):
        msg="""
        ls
        pwd
        cd .. /..
        get filename
        put filename       
        """
        print(msg)
    def cmd_put(self,*args):
        cmd_split=args[0].split()#  .split() 是将args[0]转换成列表形式
        if len(cmd_split)>1:
            filename=cmd_split[1]
            if os.path.isfile(filename):
                filesize=os.stat(filename).st_size
                msy_dict={     #用json来解析，方便扩展
                    "action":"put",
                    "filename":filename,
                    "filesize":filesize,
                    "overridden":True
                }
                self.client.send(json.dumps(msy_dict).encode("utf-8"))
                #防止黏包，等服务器确认
                server_response=self.client.recv(1024)  #返回的状况，--最好用http的标准返回
                print("server_response",server_response.decode())
                f=open(filename,"rb")
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload success ....")
                    f.close()
            else:
                print(filename,"is not exist")
    def cmd_get(self,*args):  #args[0]=get 笔记
        filename=args[0].split()[1]
        msy_dict = {  # 用json来解析，方便扩展
            "action": "get",
            "filename": filename,
            "overridden": True
        }
        self.client.send(json.dumps(msy_dict).encode("utf_8"))
        is_not_exist=self.client.recv(1024)
        if b"00"==is_not_exist:
                print("文件不存在")
        else:
            file_size = self.client.recv(1024)  # 2.收文件大小
            print("file size:", file_size.decode())  # 打印文件大小
            file_total_size = int(file_size.decode())
            self.client.send(b"ready to recv file")  # 3. 发  --准备好收文件
            received_size = 0
            f = open(filename + ".new", "wb")
            m = hashlib.md5()
            while received_size < file_total_size:
                if file_total_size - received_size >= 1024:
                    size = 1024
                else:
                    size = file_total_size - received_size
                data = self.client.recv(size)
                received_size += len(data)
                m.update(data)
                f.write(data)
            else:
                new_file_md5 = m.hexdigest()
                print("file recv done")
                f.close()
                server_file_md5 = self.client.recv(1024)
                print("new_file_md5: ", new_file_md5)
                print("server_file_md5: ", server_file_md5.decode("GBK"))
                print("file_total_size: %s,   received_size: %s" % (file_total_size, received_size))
                if file_total_size==received_size:
                    print("file get done ...")
            return self.interactive

    def authenticate(self):
        # self.name="alex"
        # self.password="123"
        while True:
            self.name = input("name>>:")
            self.password = input("password>>:")
            if ("jvzi"==self.name and "123"==self.password ):
                print("登录成功!")
                self.interactive()
            else:
                print("用户名或密码错误，请重新输入：")
ftp=FtpClient()
ftp.connection("140.143.25.160",9999)
# ftp.connection("localhost",9999)
ftp.authenticate()



