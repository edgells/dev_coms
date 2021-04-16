from concurrent.futures import ThreadPoolExecutor

import pika


def send():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.queue_declare('worker_queue', durable=True)

    ch.basic_publish(exchange='',
                     routing_key='worker_queue',
                     body=b'task ....',
                     properties=pika.BasicProperties(
                         delivery_mode=2,
                     ))

    print('message send over')
    ch.close()

def recv():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.queue_declare('worker_queue', durable=True)

    def msg_callback(ch, method, p, message):
        print(message)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    ch.basic_qos(prefetch_count=1)
    ch.basic_consume(queue='worker_queue', on_message_callback=msg_callback)
    ch.start_consuming()

if __name__ == '__main__':
    for _ in range(10):
        send()

    with ThreadPoolExecutor() as executor:
        for _ in range(5):
            executor.submit(recv)