import pika

# Config da mensageria
URL_CLOUDAMQP = "amqps://vidpgjuy:OAN8abcH8PfivUpPmdgGbtL9lxsIBmer@shark.rmq.cloudamqp.com/vidpgjuy"
parameters = pika.URLParameters(URL_CLOUDAMQP)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='fila_trabalho')

# Conteudo
print(" --- PRODUTOR INTERATIVO LIGADO ---")
print(" Digite sua mensagem e aperte Enter para enviar.")
print(" (Digite 'sair' para encerrar)\n")

try:
    while True:
        msg = input(" > Mensagem: ")
        if msg.lower() == 'sair':
            break
        channel.basic_publish(exchange='', routing_key='fila_trabalho', body=msg)
        print(f" [✔] Produtor enviou com sucesso: '{msg}'")
finally:
    connection.close()
