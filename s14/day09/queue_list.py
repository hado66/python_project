#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import  queue
# q=queue.Queue(maxsize=5)
# q=queue.LifoQueue()  #last in first out
# for i in range(10):
#     q.put(i)
# for i in range(50):
#     try:
#         print(q.get_nowait())
#     except  Exception  as e:
#         print(e)

q=queue.PriorityQueue()
q.put((1,"chen ronghua "))
q.put((2,"safdsaf"))
print(q.get())
print(q.get())