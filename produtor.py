import pika
import random

# Config da mensageria
URL_CLOUDAMQP = "amqps://vidpgjuy:OAN8abcH8PfivUpPmdgGbtL9lxsIBmer@shark.rmq.cloudamqp.com/vidpgjuy"
parameters = pika.URLParameters(URL_CLOUDAMQP)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='fila_trabalho')

# Conteudo
request_number = random.randint(1000, 9999)
msg = f"Pedido #{request_number} enviado para processamento assíncrono!"
channel.basic_publish(exchange='', routing_key='fila_trabalho', body=msg)

print(f" [✔] Produtor enviou com sucesso: '{msg}'")

connection.close()
