#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from  day12 import orm_多外键_表结构  as orm_many_fk
from sqlalchemy.orm import sessionmaker

Session_class=sessionmaker(bind=orm_many_fk.engine)#创建与数据库连接

session=Session_class()#生成session实例 #cousor

addr1=orm_many_fk.Address(street="tiantongyuan",city="changping",state="beijing")
addr2=orm_many_fk.Address(street="wudaokou",city="haidian",state="beijing")
addr3=orm_many_fk.Address(street="yanjiao",city="langfang",state="hebei")
session.add_all([addr1,addr2,addr3])


c1=orm_many_fk.Customer(name="alex",billing_address_id=addr1,shipping_address=addr2) #插入数据失败，问题未解决
# c2=orm_many_fk.Customer(name="alex",billing_address_id=addr2,shipping_address=addr2)
# c3=orm_many_fk.Customer(name="alex",billing_address_id=3,shipping_address=3)
session.add_all([c1])

session.commit()


