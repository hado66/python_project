#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
def preorder(self,root):
    """递归实现先序遍历"""
    if root==None:
        return
    print(root.elem)
    self.preorder(root.lchild)
    self.preorder(root.rchild)

def inorder(self,root):
    """递归实现中序遍历"""
    if root==None:
        return
    self.inorder(root.lchild)
    print(root.elem)
    self.inorder(root.rchild)

def postorder(self,root):
    """递归实现后续遍历"""
    if root==None:
        return
    self.postorder(root.lchild)
    self.postorder(root.rchild)
    print(root.elem)

#通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild做孩子和rchild右孩子
class Node(object):
    """节点类"""
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild

#树的创建，创建一个树的类，并给一个root根节点，一开始没空，随后添加节点
class Tree(object):
    """树类"""
    def __init__(self,root=None):
        self.root=root
    def add(self,elem):
        node=Node(elem)
        if self.root==None:
            self.root=node
        else:
            queue=[]
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur=queue.pop(0)
                if cur.lchild==None:
                    cur.lchild=node
                    return
                elif cur.rchild==None: 
                    cur.rchild=node
                    return
                else:
                    #如果左右子树不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

