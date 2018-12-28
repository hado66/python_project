#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import pika
connection=pika.BlockingConnection(pika.ConnectionParameters("localhost")) # 建立一个连接 （建立一个socket）
channel=connection.channel()  #声明一个管道
#声明queue
channel.queue_declare(queue="hello",durable=True) #声明队列   durable=Ture 队列持久化

# RabbitMQ a message can never be sent directly to the queue,it always needs to go through an exchange
channel.basic_publish(exchange='',
                      routing_key="hello",  #queue 的名字
                      body="Hello World!",#消息内容
                      properties=pika.BasicProperties(
                          delivery_mode=2, #make message persistent 消息的持久化
                      ))
print("[x] Sent ‘Hello World！’")
connection.close()  #  关闭连接----关闭队列