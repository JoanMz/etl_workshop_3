import time
import json
import pandas as pd
from kafka import KafkaProducer

# Cargar el DataFrame
df = pd.read_csv('/home/joan/Desktop/etl_workshop_3/Data/Train/df_T.csv')  # Asegúrate de usar el camino correcto a tu archivo de datos

# Configurar el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('UTF-8')
)

# Enviar datos uno por uno con un delay de 1 segundo
x=0
for index, row in df.iterrows():
    data = row.to_dict()
    producer.send('Happinessprediction', value=data)
    print(x)
    x+=1
    time.sleep(1)

print("\n [[End]] \n")
producer.close()
