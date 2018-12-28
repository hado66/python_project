#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="140.143.25.160",port=22,username="root",password="hadoop")
stdin,stdout,stderr=ssh.exec_command("ls -l")
result=stdout.read().decode("gbk")
print(result)
ssh.close()