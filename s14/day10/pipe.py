#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import multiprocessing

def f(conn):
    print(conn.recv())

    conn.send([42,None,"hello from child"])

if __name__=="__main__":
    parent_conn,child_conn=multiprocessing.Pipe()
    p=multiprocessing.Process(target=f,args=(child_conn,))
    p.start()
    parent_conn.send("I come form prarent_conn")
    print(parent_conn.recv())
