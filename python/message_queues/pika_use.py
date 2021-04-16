import pika


def pika_send():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    channel = rb_conn.channel()
    channel.queue_declare("hello")      #  create queue

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          properties=pika.BasicProperties(),        # 可以通过 properties 控制消息的属性
                          body=b'hello world')
    rb_conn.close()
    print("message send over")

def pika_recevied():
    rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                                port=5672,
                                                                virtual_host='/',
                                                                credentials=pika.PlainCredentials(username='admin',
                                                                                                  password='admin')),
                                      )
    ch = rb_conn.channel()
    ch.queue_declare('hello')

    ch.basic_consume(queue='hello',
                     auto_ack=True,
                     on_message_callback=callback)
    ch.start_consuming()

def callback(ch, method, properties, message):
    print(message.decode())

if __name__ == '__main__':
    for _ in range(10):
        pika_send()

    pika_recevied()