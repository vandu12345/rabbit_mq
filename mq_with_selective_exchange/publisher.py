# Publisher
# • Create a connection, say CN
# • Create a channel in CN, say CH
# • Create an Exchange
# • Publish the message
# • Close the connection
# • Automatically closes the channel

import time
import pika
import random

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', 5672))

# Create a channel
channel = connection.channel()

channel.exchange_declare(exchange="log_exchange", exchange_type="direct")

severity = ["Error", "Warning", "Info", "Other"]
messages = ["EMsg", "WMsg", "IMsg", "OMsg"] 

for i in range(10):
    random_num = random.randint(0, len(severity) - 1)
    print(random_num)
    message = messages[random_num]
    rk = severity[random_num]
    channel.basic_publish(exchange="log_exchange", routing_key=rk, body=message)
    print("[x] sent %r" %message)

channel.exchange_delete(exchange="log_exchange", if_unused=False)

connection.close() 
