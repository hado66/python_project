#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from  sqlalchemy import  func
import random,string

engine=create_engine("mysql+pymysql://root:jvzi@140.143.25.160/testdb",encoding="utf-8",echo=True)

Base=declarative_base() #生成orm 基类

class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    register_date=Column(String(32),nullable=False)

    def __repr__(self):
        return "<%s  name:%s  register_date:%s>" %(self.id,self.name,self.register_date)

class StudyRecord(Base):
    __tablename__="study_record"
    id=Column(Integer,primary_key=True)
    day=Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    stu_id=Column(Integer,ForeignKey("student.id"))

    student=relationship("Student",backref="my_study_record")  #把俩个类关联，存在内存中

    def __repr__(self):
        print()
        return "<%s  day:%s status:%s>" %(str(self.student.name),str(self.day),str(self.status))


Base.metadata.create_all(engine)  #创建表结构

Sesstion_class=sessionmaker(bind=engine)
session=Sesstion_class()

# s1=Student(name="alex",register_date="2015-10-15")
# s2=Student(name="tom",register_date="2015-12-15")
# s3=Student(name="jack",register_date="2015-11-15")
# s4=Student(name="xiaoqian",register_date="2013-10-15")
#
# study_obj1=StudyRecord(day=1,status="yes",stu_id=1)
# study_obj2=StudyRecord(day=2,status="yes",stu_id=1)
# study_obj3=StudyRecord(day=3,status="yes",stu_id=1)
#
# study_obj4=StudyRecord(day=1,status="yes",stu_id=2)
# study_obj5=StudyRecord(day=3,status="yes",stu_id=2)
#
# session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4,study_obj5])

stu_obj=session.query(Student).filter(Student.name=="alex").first()

print(stu_obj.my_study_record)
session.commit()

