#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import pika
connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel=connection.channel()

channel.queue_declare(queue="hello1",durable=True)

def callback(ch,method,properties,body): #四个标准参数，body是消息内容  callback是回调函数
    print("...",ch,method,properties) #ch--管道的内存对象地址 ，method一般不用
    print("[x] Received %r"%body)
channel.basic_qos(prefetch_count=1) #检测当前消息队列中有多少消息，若超过一条，不继续接受
#basic_consume 开始消费消息
channel.basic_consume(callback,    #执行这个函数  （如果收到消息，就调用callback函数，来处理消息）
                      queue="hello",  # 代表从哪个队列收消息
                      # no_ack=True   #  no ackownledgement
                      )

print("[x] Waiting for message. To exit press CTRL+C")
channel.start_consuming() #开始收消息，只要已启动，就一直运行