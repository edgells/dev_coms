import random
import threading

import pika


"""
    总结：
        
"""

def send():
    tag = random.choice(['info', 'error', 'warn'])

    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.exchange_declare(exchange='direct_logs', exchange_type='direct')      # create direct exchange
    # bind queue

    msg = b"hello world"
    for n in range(100):
        for tag in ['info', 'error', 'warn']:
            ch.basic_publish(exchange="direct_logs",
                             routing_key=tag,
                             body=msg)     # to exchange send message

    ch.close()
    print('send over')


def recv():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.exchange_declare('direct_logs', exchange_type='direct')

    def callback(ch, method, p, msg):
        print(threading.get_ident(), '---', method.routing_key, '---', msg)


    queue = ch.queue_declare(queue='', exclusive=True)
    queue_name = queue.method.queue

    for tag in ['info', 'error', 'warn']:
        ch.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=tag)

    ch.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    ch.start_consuming()

if __name__ == '__main__':
    rv = threading.Thread(target=recv)
    rv.start()

    send()

    rv.join()
