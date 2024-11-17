import threading
import kafka_producer, kafka_consumer

if __name__ == "__main__":
    t1 = threading.Thread(kafka_consumer())
    t2 = threading.Thread(kafka_producer())


    t1.start()
    t2.start()

    t1.join()
    t2.join()