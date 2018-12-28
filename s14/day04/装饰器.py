#装饰器：本质是函数---主要用来装饰>>--其他函数
#---换句话说：为其他函数添加附件功能
# 装饰器遵循的原则：1. 不能修改被装饰的函数的源代码
#                   2.不能修改函数的调用方式(不修改函数的调用方式)
#实现装饰起的知识储备：
'''
1.函数即“变量”
2.高阶函数
        a. 把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
        b.返回值中包含函数名（不修改函数的调用方式） 
3.嵌套函数


高阶函数+嵌套函数》= 装饰器
'''

#decorator
import time
# def timer(func1):
#     def warpper(*args,**kwargs):
#         start_time=time.time()
#         func1()
#         stop_time=time.time()
#         print("the func run time is %s" %(stop_time-start_time))
#     return warpper()
#
# @timer
# def test1():
#     time.sleep(1)
#     print("in the test1")
# timer(test1)
def bar():
    time.sleep(3)
    print('in the bar')
def test2(func):
    print(func)
    return func
t=test2(bar)
print(t)
print(t())

