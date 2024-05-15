# Create a connection say CN
# • Create a channel in CN, say CH
# • Create the exchange (will not affect if
# exchange is already there)
# • Create the temporary queue, if it
# does not exist already and associate it
# with the channel CH exclusively
# • Bind the queue with the exchange
# • Associate a call-back function with
# the message queue
# • Start consuming the messages


import time
import pika

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', 5672))

# Create a channel
channel = connection.channel()

# Declare an exchange
exchange_name = 'fanout_exchange'
# Will do unicast
exchange_type = 'fanout'  # 'direct', 'topic', 'headers', or 'fanout'
channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

# Don't delare a queue name
result = channel.queue_declare(queue="",exclusive=True)

queue_name = result.method.queue

print(f"Subscriber Queue Name : {queue_name}")

# Bind

channel.queue_bind(exchange=exchange_name, queue=queue_name)

print("Waiting for Message")

def callback(ch, method, properties, body):
    print("Received: %r",body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
            