#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
# import paramiko
# transport=paramiko.Transport(("192.168.100.197",22))
# transport.connect(username='hado',password='hado')
# sftp=paramiko.SFTPClient.from_transport(transport)
# sftp.put("biji","/home/hado")
# transport.close()
# #
# __author__ = "Alex Li"

import paramiko
transport = paramiko.Transport(('101.200.56.207', 9995))
transport.connect(username='jcode', password='jcode')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('笔记', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.put('biji','/home/jcode/aa')
transport.close()