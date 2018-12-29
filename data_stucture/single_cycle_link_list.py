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
                print(cur.elem,end= '')
                cur=cur.next
            # 退出循环时，cur指向尾节点，但是未打印
            print(cur.elem)
        print("")

node=Node("wo shi di yi ge jie dian")
scl=Single_Cycle_list(node)
print(scl.is_empty())
print(scl.length())
scl.traval()