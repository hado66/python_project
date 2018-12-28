#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import pika
import sys
connection =pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel=connection.channel()
channel.exchange_declare(exchange="direct_log",exchange_type="direct")

severity=sys.argv[1] if len(sys.argv)> 1 else "info"
message=''.join(sys.argv[2:]) or "hello world!"
channel.basic_publish(exchange="direct_logs",
                      routing_key=severity,
                      body=message)
print("[x] Sent %r:%r "% (severity,message))
connection.close()