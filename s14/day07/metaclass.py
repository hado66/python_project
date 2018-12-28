#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"

class MyType(type):
    def __init__(self,what,bases=None,dict=None):
        print("Mytype  __init__")
        super(MyType,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__",*args,**kwargs)
        obj=self.__new__(self)
        print("obj",obj,*args,**kwargs)

        self.__init__(obj,*args,**kwargs)
        return  obj
    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls,*args,**kwargs)

# print("here...")
print("-------------")

class Foo(object,metaclass=MyType):
# class Foo(object):            #是通过new来实例化的，，__new__ -->触发 __init__
    def __init__(self,name):
        self.name=name
        print("Foo __init__")
    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls,*args,**kwargs)
        # print(object.__new__(cls))
        return object.__new__(cls) #继承父亲的 __new__方法
f=Foo("Alex")
print(f.name)
