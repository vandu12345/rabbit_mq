import time
import pika
import pika.exceptions
import random

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', 5672))

# Create a channel
channel = connection.channel()

# Add acknowledgement so that it's acknowledges the messages
channel.confirm_delivery()

# Declare an exchange
exchange_name = 'logs_exchange'
# Will do unicast
exchange_type = 'direct'  # 'direct', 'topic', 'headers', or 'fanout'
channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True)

 
severity = ["Error", "Warning", "Info", "Other"]
messages = ["EMsg", "WMsg", "IMsg", "OMsg"] 

for i in range(10):
    random_num = random.randint(0, len(severity) - 1)
    print(random_num)
    message = messages[random_num]
    rk = severity[random_num]
    try:
        # Make message persistent
        channel.basic_publish(exchange=exchange_name, routing_key=rk, body=message,properties=pika.BasicProperties(delivery_mode=2))
        print(f"Sent : {message}")
    except pika.exceptions.ChannelClosed as err_msg:
        print(f"Channel Closed: {err_msg}")
    except pika.exceptions.ConnectionClosed as err_msg:
        print(f"Connection Closed: {err_msg}")

channel.exchange_delete(exchange=exchange_name, if_unused=False)

connection.close()
