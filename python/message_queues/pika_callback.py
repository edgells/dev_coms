import time

import pika
from pika.channel import Channel


"""
    non blocking send message
"""

def on_open(connection):
    connection.channel(on_open_callback=on_channel_open)


def on_channel_open(channel: Channel):
    while 1:
        time.sleep(0.1)
        channel.basic_publish('', 'worker_queue', b'select message', pika.BasicProperties(content_type='text/plain', type='example'))

# 使用 select 方式的connection
connection = pika.SelectConnection(parameters=pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      on_open_callback=on_open)


try:
    connection.ioloop.start()

except KeyboardInterrupt as e:
    connection.close()

    connection.ioloop.start()