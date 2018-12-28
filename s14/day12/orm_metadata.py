#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from sqlalchemy import Table,MetaData,Column,Integer,String
from sqlalchemy.orm import mapper

metadata=MetaData()

user1=Table("user1",metadata,
            Column("id",Integer,primary_key=True),
            Column("name",String(50)),
            Column("fullname",String(50)),
            Column("password",String(50))
            )

class User(object):
    def __init__(self,name,fullname,password):
        self.name=name
        self.fullname=name
        self.password=password

mapper(User,user1)