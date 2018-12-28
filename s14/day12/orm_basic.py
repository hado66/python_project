#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import random,string

engine=create_engine("mysql+pymysql://root:jvzi@140.143.25.160/testdb",encoding="utf_8",echo=True)#连上

Base=declarative_base() #生成orm基类

class User(Base):                #-----生成这个表结构，创建这个表结构
    __tablename__="user1" #表名
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    password=Column(String(32))
    def __repr__(self):
        return "<%s name:%s  password:%s>"%(self.id,self.name,self.password)


Base.metadata.create_all(engine)#创建表结构

#（以上是创建表）
#+++++++++++++++++++++++------------------==========================
#（一下是创建数据）

Session_class=sessionmaker(bind=engine)#创建与数据库的会话session class ，注意：：注意,这里返回给session的是个class,不是实例
Session=Session_class() #生成session实例

# for i in range(500):  """创建数据"""
#     passwd = ''.join(random.sample(string.ascii_letters + string.digits + "!@#$%^&*()_+", 6))
#     user_obj=User(name="wzy"+str(i),password=passwd)
#     print(user_obj.name,user_obj.id) #此时还没创建对象呢，现在的id还为空
#
#     Session.add(user_obj)
#     print(user_obj.name,user_obj.id) #此时也没有创建，因为还没有commit

# data=Session.query(User).filter(User.id>1).count()
# print(data)
# data[0].name="dongqian"
# data[0].password="yuan668668"
# Session.commit()
data=Session.query(func.count(User.name),User.name).group_by(User.name).all()
print(data)