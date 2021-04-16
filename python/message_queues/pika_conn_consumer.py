import pika



rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                            port=5672,
                                                            virtual_host='/',
                                                            credentials=pika.PlainCredentials(username='admin',
                                                                                              password='admin')),
                                  )
ch = rb_conn.channel()

def on_message(ch, method, p, msg):
    print(msg.decode())


ch.basic_consume('worker_queue', on_message)
try:
    ch.start_consuming()

except:
    ch.stop_consuming()

finally:
    rb_conn.close()