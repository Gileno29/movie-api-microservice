
import os
from confluent_kafka import Consumer, KafkaError
# Configurações do Kafka
KAFKA_CONFIG = {
    'bootstrap.servers':os.environ("SERVER"),  # Altere para o endereço do seu Kafka
    'group.id': os.environ("GROUP"),       # ID único do seu consumidor
    'auto.offset.reset': os.environ("OFFSET")        # Começa a ler do início se não houver offset salvo
}

# Tópico Kafka onde sua API Go está publicando
#KAFKA_TOPIC = 'books_created' 
def consume_and_save():
    TOPIC=os.environ("TOPIC")
    consumer = Consumer(KAFKA_CONFIG)
    consumer.subscribe([TOPIC])

    print(f"[*] Consumidor Kafka iniciado no tópico: {TOPIC}")

    try:
        while True:
            # Pega uma mensagem, timeout de 1.0 segundo
            msg = consumer.poll(1.0) 

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # Fim da partição (não é um erro real)
                    continue
                else:
                    print(f"Erro do Consumidor: {msg.error()}")
                    break

            # 1. Desserializar a mensagem (assumindo que sua API Go envia JSON)
            try:
                book_data = json.loads(msg.value().decode('utf-8'))
                print(f"Recebido livro: {book_data.get('title')}")

                # 2. Lógica de Persistência no DB
                save_to_database(book_data) 
                
            except Exception as e:
                print(f"Erro ao processar mensagem: {e}")

    except KeyboardInterrupt:
        pass
    finally:
        # Garante que o consumidor se desconecte de forma limpa
        consumer.close()
        print("\nConsumidor encerrado.")


def save_to_database(book_data):
    """
    Simulação da lógica para salvar no banco de dados.
    Aqui é onde você usaria seu driver DB ou ORM (SQLAlchemy).
    """
    
    # Exemplo: Usando SQL puro (apenas um esboço)
    # conn = engine.connect()
    # conn.execute(
    #    "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)",
    #    (book_data['title'], book_data['author'], book_data['isbn'])
    # )
    # conn.close()
    
    print(f"   -> Livro '{book_data.get('title')}' salvo no DB (simulado).")