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
            while cur.next!=self.__head:
                count+=1
                cur=cur.next
            return count

    def traval(self):
        """遍历整个链表"""
        if self.is_empty():
            return None
        else:
            cur=self.__head
            while cur.next!=self.__head:
                print(cur.elem,end= ' ')
                cur=cur.next
            # 退出循环时，cur指向尾节点，但是未打印
            print(cur.elem)
        print("")
    def add(self,item):
        """从头部插入"""
        node=Node(item)
        cur=self.__head
        if self.is_empty():#链表为空时
            self.__head=node
            node.next=node
        else:
            while cur.next!=self.__head:
                cur=cur.next
            #退出循环时，cur指向最后一个节点
            node.next=self.__head
            self.__head=node
            # cur.next=node
            cur.next=self.__head
    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=self.__head
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            node.next = self.__head
            cur.next=node

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



# node=Node("wo shi di yi ge jie dian")
# scl=Single_Cycle_list(node)
# scl.add(1)
# scl.add(2)
# scl.append(9)
scl=Single_Cycle_list()
scl.add(4)
scl.add(1)
scl.add(2)
scl.append(9)
scl.traval()
scl.insert(2,"churu")
print(scl.is_empty())
print(scl.length())
scl.traval()