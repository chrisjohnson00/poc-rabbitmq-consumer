# example_consumer.py
import pika
import os

# Access the AMQP_URL environment variable and parse it
url = os.environ.get('AMQP_URL')
print(url)
params = pika.URLParameters(url)
print(params)
connection = pika.BlockingConnection(params)
print(connection)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='chris_test')  # Declare a queue
print(channel)
print("Done")