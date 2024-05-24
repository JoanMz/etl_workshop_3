import sys
sys.path.append("/home/joan/Desktop/etl_workshop_3/DB_connection")
import Pysqlconnect
import json
import joblib
import pandas as pd
from kafka import KafkaConsumer
import time


# Cargar el modelo guardado
model = joblib.load('/home/joan/Desktop/etl_workshop_3/Model/linear_regression_model.pkl')

# Configurar el consumidor de Kafka
consumer = KafkaConsumer(
    'Happinessprediction',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Inicializar un DataFrame para almacenar los resultados
results_df = pd.DataFrame(columns=['GDP', 'Family', 'Life Expectancy', 'Freedom', 'Trust', '2015', '2016', '2017', '2018', '2019',
          'Western Europe', 'North America', 'Australia and New Zealand', 'Middle East and Northern Africa',
          'Latin America and Caribbean', 'Southeastern Asia', 'Central and Eastern Europe', 'Eastern Asia',
          'Sub-Saharan Africa', 'Southern Asia', 'Score', 'Predicted_Score'])

# Leer datos del consumidor, predecir y almacenar en el DataFrame
coh=0
count=0
for message in consumer:
    data = message.value
    X_new = pd.DataFrame([data], columns=['GDP', 'Family', 'Life Expectancy', 'Freedom', 'Trust', '2015', '2016', '2017', '2018', '2019',
          'Western Europe', 'North America', 'Australia and New Zealand', 'Middle East and Northern Africa',
          'Latin America and Caribbean', 'Southeastern Asia', 'Central and Eastern Europe', 'Eastern Asia',
          'Sub-Saharan Africa', 'Southern Asia'])
    
    # Eliminar filas con valores NaN
    if X_new.isnull().values.any():
        #print(f"Data with NaN values: {X_new}")
        print(f"{coh} errS")
        coh +=1
        continue
    
    predicted_score = model.predict(X_new)[0]
    data['Predicted_Score'] = predicted_score
    results_df = pd.concat([results_df, pd.DataFrame([data])], ignore_index=True)

    y_true = results_df['Score']
    y_pred = results_df['Predicted_Score']

    shap = y_pred.value_counts().count() -1
    print(f"Value to predict : {y_true.iloc[shap]}   Predict value: {y_pred.iloc[shap]}")
    count+=1
    if count >= 20:
        results_df.to_sql("datakafka", Pysqlconnect.connection(), if_exists="append", index=False)
        count = 0
        print("\n [data load] \n")
        time.sleep(1)