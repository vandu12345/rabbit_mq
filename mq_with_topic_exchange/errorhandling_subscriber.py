# Subscriber
# • Create a connection say CN
# • Create a channel in CN, say CH
# • Create the topic exchange (will not
# affect if exchange is already there)
# • Create the queue, if it does not exist
# already and associate it with the
# channel CH
# • Bind the queue with the exchange for
# the required Routing Key(s)
# • Associate a call-back function with
# the message queue
# • Start consuming the messages


import time
import pika
import random

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', 5672))

# Create a channel
channel = connection.channel()

channel.exchange_declare(exchange="system_exchange", exchange_type="topic")

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue



channel.queue_bind(exchange="system_exchange", queue=queue_name, routing_key='E.#')


print("Waiting For Message")

def callback(ch, method, properties, body):
    print('[x] Alarm from C2 Action::::%r'%body)
    
channel.basic_consume(queue=queue_name,on_message_callback=callback,auto_ack=True)

channel.start_consuming()


