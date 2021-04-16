import threading
from concurrent.futures import ThreadPoolExecutor

import pika

"""
    
"""

def send():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.exchange_declare(exchange='logs', exchange_type='fanout')

    message = b"info: Hello World!"

    for n in range(1000):
        ch.basic_publish(exchange='logs', routing_key='', body=message)
    rb_conn.close()


def recv(rv):
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.exchange_declare(exchange='logs', exchange_type='fanout')        # 订阅指定的exchange

    result= ch.queue_declare(queue="", exclusive=True)                  # 创建指定的 queue
    queue_name = result.method.queue
    ch.queue_bind(exchange='logs', queue=queue_name)                    # 将queue 与 exchange 绑定


    def callback(ch, method, p, message):
        print(threading.current_thread().ident, message)

    ch.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    ch.start_consuming()


if __name__ == '__main__':

    t = threading.Thread(target=send)
    t.start()

    r1 = threading.Thread(target=recv, args=(1, ))
    r2 = threading.Thread(target=recv, args=(2, ))

    r1.start()
    r2.start()


    t.join()
    r1.join()
    r2.join()