#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from multiprocessing import Process
import os
def info(title):
    print(title)
    print("module name",__name__)
    print("parent process",os.getppid())
    print("process id:",os.getpid())
    print("\n")
def run(name):
    info("\033[32;1main process line\033[0m")
    print("hello",name)

if __name__=="__main__":
    info("\033[32;1mnain process line \033[0m")
    p=Process(target=run,args=("sadfs",))
    p.start()
    p.join()