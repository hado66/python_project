# #!/usr/bin/python
# #-*- coding: utf-8 -*-
# #__author__="Ziyuan Wang"
# import sys
# import pika
# connection=pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
# channel=connection.channel()
#
# channel.exchange_declare(exchange="logs",exchange_type='fanout')
#
# msg='  '.join(sys.argv[1:])or "Hello World!" #通过命令行调用，自己输入消息，否则是hello world
# channel.basic_publish(exchange="logs",
#                       routing_key="",
#                       body=msg,
#                       # properties=pika.BasicProperties(
#                       #     delivery_mode=2,
#                       # )
#                       )
# print("[x ] sent % r" %msg)
# connection.close()
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()