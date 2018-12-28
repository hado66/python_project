#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import pymysql
data=[
    ("N1",25,"M"),
    ("N2",20,"f"),
    ("N3",24,"M"),
]
conn=pymysql.connect(host="140.143.25.160",port=3306,user="root",passwd="jvzi",db="testdb")
# conn=pymysql.connect("140.143.25.160",3306,"root","jvzi","testdb")

cursor=conn.cursor( )
# effect_now=cursor.execute("select * from student")
# print(effect_now)
# print(cursor.fetchone())
# print("所有：",cursor.fetchall())
# cursor.executemany("insert into student (name,age,sex) VALUES (%s,%s,%s)",data)
conn.commit()
effect_now=cursor.execute("select * from student")

print(cursor.fetchall())


