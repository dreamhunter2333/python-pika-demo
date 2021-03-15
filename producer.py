#!/usr/bin/env python
import pika

auth = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='pika_host',
    port=5672,
    virtual_host='/demo',
    credentials=auth
))
channel = connection.channel()

channel.queue_declare(queue='TEST03', durable=True)


for i in range(1000):
    channel.basic_publish(
        exchange='',
        routing_key='TEST03',
        body='Hello World!' + str(i),
        properties=pika.BasicProperties(delivery_mode=2)
    )
connection.close()
