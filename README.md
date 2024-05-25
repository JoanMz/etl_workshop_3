<h1 align="center">🐿️etl_workshop_3🐿️</h1>

![joanmz_ardilla_8bd01766-16a6-4595-a86a-25b8147143d5](https://github.com/JoanMz/etl_workshop_3/assets/103477035/2dc296ca-af77-4197-9444-949b304f4b76)
---
Machine Learning and Data Streaming. The main goal is to develop a regression machine learning model that predicts the happiness score of different countries based on data provided in five CSV files. The project involves comprehensive exploratory data analysis (EDA) and extract, transform, load (ETL) processes to extract relevant features from the data. Using technologies such `Python`, `Apache kafka`, `ScikitLearn`, `Postgres`, `Docker`

Workflow
- Data Preprocessing: Conduct EDA and ETL to clean and prepare the data.
- Model Training: Train a regression model using a 70-30 data split (70% for training and 30% for testing).
- Data Streaming: Stream the transformed data using Kafka.
- Prediction: Use the trained model to predict happiness scores on the testing dataset.
- Storage: Store the predictions along with the input features in a database.
- Evaluation: Extract performance metrics to evaluate the model's accuracy using the testing data and the predicted data.

## Data
The dataset consists of five CSV files containing happiness information for different countries over various years. Note that data from different years may have variations, requiring careful evaluation and comparison of features across datasets.

### Technologies Used
- Python
- Jupyter Notebook
- Kafka
- Scikit-learn library
- Database (Postgres)
- CSV files
- Docker

## Installation

Follow these steps to set up the project:

1. **Install and Verify WSL**:
   - [WSL Installation Guide](https://docs.microsoft.com/en-us/learn/modules/get-started-with-windows-subsystem-for-linux/)


2. **Install Required Programs**:
   - Install Python 3
   - Install Docker: [Docker Engine Installation Guide](https://docs.docker.com/engine/install/ubuntu/)

3. **Create virtualenv**:
   ```bash
   python3 -m venv venv
   ```
   - Activate the virtual env:
     ```bash
     source venv/bin/activate
     ```
   - Install Apache Kafka via pip:
     ```bash
     pip install kafka-python
     pip install -r requirements.txt
     ```

5. **Create Password Files and Virtual Environment**:
   - Create the necessary password files (`./.env`, `./DB_connection/docker-secrets`)
  
     
3. **Download Docker Image for the Database**:
   - Into DB_connection directory run the PostgreSQL compose  with the image and configurations: 
     ```bash
     #At /DB_connection
     sudo docker compose up
     ```
  - Into Kafka directory run the docker-compose.yml file with the kafka environment
    ```bash
    #At /Kafka
    sudo docker compose up
    ```
