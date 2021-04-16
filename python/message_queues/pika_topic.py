import threading

import pika


def send():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()

    ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

    routing_key = "info.dev.log"
    message = b"hello world"

    for n in range(100):
        ch.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

    ch.close()


def recv():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

    result = ch.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    ch.queue_bind(exchange='topic_logs', routing_key='*.*.*', queue=queue_name)

    def callback(ch, method, p, msg):
        print(method.routing_key, '--', msg)

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
