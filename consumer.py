import pika


def main():
    # create a connection
    connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0',5672))

    # create a channel over the connection
    channel = connection.channel()
    
    # create queue
    channel.queue_declare("suvvu")

    def callback(ch, method, properties, body):
        print(f"[x] received {str(body)}")

    # Associate a callback function to the queue
    channel.basic_consume(queue="suvvu", on_message_callback=callback, auto_ack=True)
    
    # Start Consuming the message
    channel.start_consuming()

    

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Broken")
        