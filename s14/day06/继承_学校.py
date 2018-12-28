#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
#  学校、讲师、学院

class School(object):
    def __init__(self,name,addr):
        self.Name=name
        self.Addr=addr
        self.Students=[]
        self.Teachers=[]
    def enroll(self,stu_obj):
        print("为学员%s 办理注册手续"%stu_obj.Name)
        self.Students.append(stu_obj)
    def pay_suition(self,staff_obj):
        print("雇佣新员工%s"%staff_obj.Name)
        self.Teachers.append(staff_obj)


class SchoolMenber(object):
    def __init__(self,name,age,sex):
        self.Name=name
        self.Age=age
        self.Sex=sex
    def tell(self):
        pass


class Teacher(SchoolMenber):
    def __init__(self,name,age,sex,tea_id,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.tea_id=tea_id
        self.Salary=salary
        self.Course=course
    def tell(self):
        print("""
        ----the teacher of info %s-----
         Name:%s
         Sex:%s
         Tea_Id:%s
         Salary:%s
         Course:%s
         """ %(self.Name,self.Name,self.Sex,self.tea_id,self.Salary,self.Course))
    def teach(self):
        print("%s is teaching course [%s]"%(self.Name,self.Course) )



class Student(SchoolMenber):
    # def __init__(self,name,age,sex,stu_id,grade):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        #SchoolMenber.__init__(self,name,age,sex)   经典类
        self.stu_id=stu_id
        self.Grade=grade
    def tell(self):
        print("""
        ----the student of info %s-----
         Name:%s
         Sex:%s
         Stu_Id:%s
         Grade:%s
         """ %(self.Name,self.Name,self.Sex,self.stu_id,self.Grade))
    def pay_tuition(self,amount):
        print("%s has paid tuition for $%s"%(self.Name,amount))

school=School("河北科技大学","裕华区裕翔街26号")

t1=Teacher("Oldboy",56,"MF","00000244",2000000,"Linux")

s1=Student("wangziyuan",22,"m","141004113","信科141")
t1.tell()
s1.tell()
school.enroll(s1)
school.pay_suition(t1)
school.Teachers[0].teach()
school.Students[0].pay_tuition(10000)

