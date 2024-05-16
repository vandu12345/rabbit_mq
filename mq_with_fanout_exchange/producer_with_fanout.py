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

 
for i in range(4):
    message = f"Hello World {i}" 
    channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
    print(f"Sent : {message}")

channel.exchange_delete(exchange=exchange_name, if_unused=False)

connection.close()
