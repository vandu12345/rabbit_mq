# Publisher
# • Create a connection, say CN
# • Create a channel in CN, say CH
# create exchange
# • Publish the message
# • Close the connection
# • Automatically closes the channel
# • Subscriber
# •


import time
import pika

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', 5672))

# Create a channel
channel = connection.channel()

# Declare an exchange
exchange_name = 'test_exchange'
# Will do unicast
exchange_type = 'direct'  # 'direct', 'topic', 'headers', or 'fanout'
channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

# Declare a queue
queue_name = 'suvvu'
channel.queue_declare(queue=queue_name)

# Bind the queue to the exchange
routing_key = 'my_routing_key'
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# Publish a message to the exchange with the routing key
message = 'Hello World Message #5'
channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

print(f"Sent: {message}")


time.sleep(120) 
# Close the connection
connection.close() 


