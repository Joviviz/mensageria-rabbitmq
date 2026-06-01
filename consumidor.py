import pika
import sys
import os

def main():
    # Config da mensageria
    URL_CLOUDAMQP = "" # Inserir o URL do AMQP
    parameters = pika.URLParameters(URL_CLOUDAMQP)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='fila_trabalho')

    def callback(ch, method, properties, body):
        print(f" [🖨] Consumidor recebeu da nuvem: {body.decode()}")
        print(" [-->] Processando tarefa no microsserviço... Concluído!\n")

    channel.basic_consume(queue='fila_trabalho', on_message_callback=callback, auto_ack=True)

    print(' [*] Conectado à Nuvem. Aguardando mensagens. Para sair pressione CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nEncerrando consumidor...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)