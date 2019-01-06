#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from singe_link_list import SingeLinkList
class Node():
    def __init__(self,item):
        self.elem=item
        self.next=None
        self.pre=None
# class DoubleLinkList(object):
#     def __init__(self,node=None):
#         self.__head=node

"""采用继承的方法"""
class DoubleLinkList(object):
    def __init__(self,node=None):
        self.__head=node
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None
    def length(self):
        """计算链表的长度"""
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            cur=cur.next
        print("")
    def insert(self,pos,item):
        node=Node(item)
        if pos<=0:
            self.add(item)
        elif pos>=self.length():
            self.apppend(item)
        else:
            cur=self.__head
            count=0
            while count<pos:
                count+=1
                cur=cur.next
            node.next=cur
            node.pre=cur.pre
            cur.pre.next=node
            cur.pre=node

    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self.apppend(item)
        else:
            cur=self.__head
            node.next=cur
            self.__head=node
            node.next.pre=node
    def apppend(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            node.pre=cur
    def search(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False
    def remove(self,item):
        cur=self.__head
        while cur.next!=None:
            if cur.elem==item :
                #判断是不是头结点
                if cur==self.__head:
                    self.__head=cur.next
                    cur.next.pre=None
                else:
                    #中间节点
                    cur.pre.next=cur.next
                    cur.next.pre=cur.pre
                    break
            cur=cur.next
        #当前cur指向最后一个节点
        if cur.elem==item and cur.next==None:
            if self.length()!=1:
                cur.pre.next=None
            else:
                self.__head=None
    def alter(self,pos,item):
        #只考虑更改中间节点的情况
        if pos<0:
            return False
        elif pos>self.length():
            return False
        else:
            node=Node(item)
            cur=self.__head
            count=0
            while cur!=None:
                if count==pos:
                    node.pre=cur.pre
                    node.next=cur.next
                    cur.pre.next=node
                    cur.next.pre=node
                count += 1
                cur=cur.next



if __name__ =="__main__":
    # node1=Node("aa")
    dll=DoubleLinkList()
    dll.add("bb")
    dll.add("cc")
    dll.apppend("dd")
    dll.apppend("ee")
    dll.insert(2,"insert")
    dll.travel()
    dll.remove("ee")
    dll.alter(1,"genggai")
    print(dll.search("ee"))
    print(dll.is_empty())
    print(dll.length())
    dll.travel()