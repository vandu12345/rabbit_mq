import time
import pika

# create a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0',5672))

# create a channel over the connection
channel = connection.channel()


#TODO:  Create a exchange and specify the bindings
# Using default exchange


# create queue
channel.queue_declare("suvvu")

# publish the message
channel.basic_publish(exchange="", routing_key="suvvu",body="Hello World Message #5")

print("Sent Message")

# Close the connection
connection.close()

# Show Queues and messages
# rabbitmqctl list_queues

