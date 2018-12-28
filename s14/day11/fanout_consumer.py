# #!/usr/bin/python
# #-*- coding: utf-8 -*-
# #__author__="Ziyuan Wang"
# import pika
# connection=pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
# channel=connection.channel()
#
# channel.exchange_declare(exchange="logs",exchange_type="fanout")
#
# result=channel.queue_declare(exclusive=True)  #exclusive  排他的，唯一的
# queue_name=result.method.queue
# print("random queuename",queue_name)
#
# channel.queue_bind(exchange="logs",queue=queue_name)
#
# print("[*] Waiting for logs . To exit press CTRL+C")
#
# channel.basic_consume(callable,
#                       queue=queue_name,
#                       no_ack=True)
# channel.start_consuming()
# _*_coding:utf-8_*_
__author__ = 'Alex Li'
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
