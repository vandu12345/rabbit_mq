# Publisher
# • Create a connection, say CN
# • Create a channel in CN, say CH
# • Create a Topic Exchange
# • Publish the message
# • Close the connection
# • Automatically closes the channel


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

channel.exchange_declare(exchange="system_exchange", exchange_type="topic")

severity = ["E", "W", "I"]
priority = ["H", "M", "L"]
action = ["A1", "A2", "A3"]
component = ["C1", "C2", "C3"] 

for i in range(10):
    random_num = random.randint(0, len(severity) - 1)
    rk = f"{severity[random.randint(0, len(severity) - 1)]}.{priority[random.randint(0, len(priority) - 1)]}.{action[random.randint(0, len(action) - 1)]}.{component[random.randint(0, len(component) - 1)]}"
    
    message = f"Message:::::::::{rk}"
    channel.basic_publish(exchange="system_exchange", routing_key=rk, body=message)
    print("[x] sent %r" %message)

# channel.exchange_delete(exchange="system_exchange", if_unused=False)

connection.close() 

