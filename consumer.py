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

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 如果该消费者的channel上未确认的消息数达到了prefetch_count数，则不向该消费者发送消息
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback,
                      queue='TEST03',
                      auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
