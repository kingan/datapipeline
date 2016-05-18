from kafka import KafkaConsumer

class kafkaConsumer(self):
    def __init__(self):
        self.var = 1
        self.consumer = KafkaConsumer('first')

    def runKafkaConsumer(self):
        

if __name__ == "__main__":
    k = kafkaConsumer()
    k.runKafkaConsumer()
