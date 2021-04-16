import pika



rb_conn = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.101.129',
                                                            port=5672,
                                                            virtual_host='/',
                                                            credentials=pika.PlainCredentials(username='admin',
                                                                                              password='admin')),
                                  )
ch = rb_conn.channel()

while 1:
    mt, header_frame, body = ch.basic_get('worker_queue', auto_ack=True)
    if mt:
        print(mt, header_frame, body)
        ch.basic_ack(mt.delivery_tag)

    else:
        print("no message returned")