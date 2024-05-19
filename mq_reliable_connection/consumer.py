# Subscriber
# • Create a connection say CN
# • Create a channel in CN, say CH
# • Create the exchange (will not affect if
# exchange is already there)
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

channel.exchange_declare(exchange="logs_exchange", exchange_type="direct", durable=True)

queue_name = 'task_queue'
result = channel.queue_declare(queue=queue_name, durable=True)


severity = ["Error", "Warning", "Info", "Other"]

for s in severity:
    channel.queue_bind(exchange="logs_exchange", queue=queue_name, routing_key=s)


print("[*] Waiting For Message")

def callback(ch, method, properties, body):
    
    print('[x] Received message::::%r'%body)
    # randomSleep = random.randint(1, 5)
    randomSleep = 5
    print(f"Working for {randomSleep} seconds")
    
    while randomSleep > 0:
        print(".", end="")
        time.sleep(1)
        randomSleep-=1
    print("!")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,on_message_callback=callback)

channel.start_consuming()




