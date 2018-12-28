class Node(object):  # 节点类   定义节点类
    def __init__(self, elem):
        self.elem = elem
        self.next = None
    #单链表
class SingeLinkList(object):  # 链表类   作用把节点串联起来
    def __init__(self, node=None):
        self.__head = node  # 加一下划线，指的是私有的

    # 链表是否为空
    def is_empty(self):
        return self.__head==None

    # 链表长度
    def length(self):
        #用游标移动遍历节点
        cur=self.__head
        #count记录数量
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    # 遍历整个链表
    def travel(self):
        cur= self.__head
        while cur!=None:
            print(cur.elem,end=' ')
            cur=cur.next
        print("")





    def add(self,item):
        # 链表头部添加元素
        node=Node(item)
        node.next=self.__head
        self.__head=node


    # 链表尾部添加元素  ,,尾插法
    def append(self, item):
        node = Node(item)
        if self.__head==None:
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def insert(self, pos, item):
        # 指定位置添加元素
        node=Node(item)
        if pos<=0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
            node.next=pre.next
            pre.next=node

    def remove(self, item):
        # remove(item) 删除节点
        pass

    def search(self,item):
        # 查找节点是否存在
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False


if __name__=="__main__":
    ll=SingeLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.travel()
    print(ll.length())
    ll.insert(5,"charu")


    print(ll.is_empty())

    print(ll.search("charu"))
    ll.travel()