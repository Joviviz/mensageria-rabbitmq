# Projeto de Mensageria Assíncrona com RabbitMQ

Este projeto foi desenvolvido para a disciplina de **Arquitetura de Sistemas Distribuídos**. 
Ele demonstra a implementação prática de um padrão de arquitetura orientada a eventos (EDA) utilizando o **RabbitMQ** como message broker hospedado na nuvem (CloudAMQP).
O objetivo é simular o desacoplamento de serviços de um e-commerce: um serviço de **Produtor** envia requisições de pedidos de forma assíncrona para uma fila, 
e um serviço **Consumidor** processa essas tarefas sob demanda, garantindo resiliência e escalabilidade.


## Arquitetura do Sistema
O sistema é composto por três pilares principais:
1. **Produtor (`produtor.py`):** Gera um número de pedido dinâmico e envia o payload para a fila `fila_trabalho`.
2. **Message Broker (RabbitMQ na Nuvem):** Gerencia a fila, garante a entrega das mensagens e fornece persistência caso o consumidor esteja offline.
3. **Consumidor (`consumidor.py`):** Fica em escuta ativa (loop) conectado ao broker para processar os pedidos em tempo real assim que chegam.

## Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Biblioteca de Conexão:** [Pika](https://pika.readthedocs.io/) (Cliente AMQP oficial para Python)
* **Message Broker:** Apache RabbitMQ (via CloudAMQP)
* **Ambiente de Execução:** GitHub Codespaces (Ambiente virtualizado em nuvem) / Docker (para testes locais)


## Como Executar o Projeto (Via GitHub Codespaces)

Como o projeto está totalmente integrado à nuvem, você pode executá-lo diretamente pelo navegador sem instalar nada localmente:

### 1. Preparação do Ambiente
Abra o terminal integrado do seu ambiente e instale a dependência do projeto:
```bash
pip install pika
```

### 2. Executando o Consumidor
Inicie o serviço que ficará escutando a fila à espera de novas mensagens:
```bash
python3 consumidor.py
```

### 3. Executando o Produtor
Em um terminal separado (ou dividindo a tela do terminal do Codespaces), execute o produtor para disparar um novo pedido com ID aleatório:
```bash
python3 produtor.py
```
