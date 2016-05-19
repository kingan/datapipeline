from kafka import KafkaConsumer
import pymongo
from pymongo import MongoClient
import sys

class kafkaConsumer():
    def __init__(self):
        self.var = 1
        self.consumer = KafkaConsumer('first')
#        self.client = MongoClient("172.31.46.29:27017")
        self.client = MongoClient("localhost:27017")
        self.db = self.client.datapipeline

    def runKafkaConsumer(self):
        try:
            while(self.consumer.next()):
                tmp = self.consumer.next()
                self.db.data0.insert({"offset":tmp.offset,"partition":tmp.partition,"topic":tmp.topic,"value":tmp.value})
        except:
            sys.exit()

    def checkMongo(self):
        print self.db.data0.find().next()

if __name__ == "__main__":
    k = kafkaConsumer()
    k.runKafkaConsumer()
#    k.checkMongo()
