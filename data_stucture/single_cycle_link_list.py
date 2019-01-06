import time
class Node(object):
    def __init__(self,item):
        self.elem=item
        self.next=None
class Single_Cycle_list(object):
    """单项循环链表"""
    def __init__(self,node=None):
        self.__head = node
        if node: #如果传了参数，不仅挂上去，而且还要指向自己（设置回环）
            node.next=node
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head==None
    def length(self):
        """计算链表长度"""
        if self.is_empty():
            return 0
        else:
            #用游标移动遍历节点
            cur=self.__head
            #用count记录数量
            count=1
            if cur.next==None:
                return 1
            while cur.next!=self.__head:
                count+=1
                cur=cur.next
            return count

    def traval(self):
        """遍历整个链表"""
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem)
            cur = cur.next
        print(cur.elem)

    # def add(self,item):
    #     """从头部插入"""
    #     node=Node(item)
    #     cur=self.__head
    #     print("add",self.__head)
    #     if self.is_empty():#链表为空时
    #         self.__head=node
    #         node.next=node
    #     else:
    #         while cur.next!=self.__head:
    #             cur=cur.next
    #         #退出循环时，cur指向最后一个节点
    #         node.next=self.__head
    #         self.__head=node
    #         # cur.next=node
    #         cur.next=node
    def add(self,item):
        """从头部插入"""
        node=Node(item)
        if self.is_empty():#链表为空时
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            node.next=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            #退出循环时，cur指向最后一个节点
            cur.next=node
            self.__head=node
    def append(self,item):
        """从尾部添加节点"""
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=self.__head
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            cur.next=node
            node.next = self.__head


    def insert(self, pos, item):
            # 指定位置添加元素
            node = Node(item)
            if pos <= 0:
                self.add(item)
            elif pos > self.length() - 1:
                self.append(item)
            else:
                pre = self.__head
                count = 0
                while count < (pos - 1):
                    count += 1
                    pre = pre.next
                node.next = pre.next
                pre.next = node
    def search(self,item):
        """查找元素是否存在"""
        if self.is_empty():
            return False
        cur=self.__head
        while cur.next!=self.__head:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        #退出循环，判断尾节点
        if cur.elem==item:
            return True
        else:
            return False
    def remove(self,item):
        """移除节点"""
        cur=self.__head
        pre=None
        while cur.next!=self.__head:
            if cur.elem==item:
                #先判度是否为头节点
                print("traval")
                if cur==self.__head and self.length()!=1:
                    #头节点的情况
                    #找尾节点
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.next
                    self.__head=cur.next
                    rear.next=self.__head
                    return
                else:
                    #中间节点
                    pre.next=cur.next
                    break
            else:
                pre=cur
                cur=cur.next
        #退出循环，代表的是cur指向尾节点
        if cur.elem==item and cur.next==self.__head:
            #只有一个节点
            if self.length()==1:
                #链表中只有一个节点
                self.__head=None
            else:
                pre.next=self.__head
    def remove_test(self,item):
        cur=self.__head
        pre=None
        while cur.next!=self.__head:
            if cur.elem==item:
                pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next

# node=Node("wo shi di yi ge jie dian")
# scl=Single_Cycle_list(node)
# scl.add(1)
# scl.add(2)
# scl.append(9)
scl=Single_Cycle_list()
scl.add(4)
scl.add(1)
# scl.add(2)
scl.append(9)
scl.traval()
scl.insert(2,"churu")
print(scl.is_empty())
print(scl.length())
print("+++")
scl.traval()
scl.remove(1)
print("================")
scl.remove(9)
scl.append(100)
scl.add("tou")
scl.remove("churu")
scl.traval()
