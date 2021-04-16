import pika
from pika.channel import Channel

def on_open(connection: pika.SelectConnection):
    connection.channel(on_open_callback=on_channel_open)

def on_channel_open(channel: Channel):
    channel.queue_declare('worker_queue', exclusive=True)
    channel.basic_consume('worker_queue', on_message_callback=on_message, auto_ack=True)
    channel.start_consuming()

def on_message(ch, method, p, msg):
    print(msg.decode())

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