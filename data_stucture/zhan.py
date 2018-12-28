
"""
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数

"""
class Stack(object):
    def __init__(self):
        self.list=[]

    def push(self,item):
        self.list.append(item)

    def pop(self):
        self.list.pop()
    def peek(self):
        if self.list:
            return self.list[-1]
        else:
            return None
    def is_empty(self):
        return self.list!=[]
    def size(self):
        return len(self.list)

if __name__=="__main__":
    s=Stack()
    s.push('safsafsa')
    print(s.is_empty())



