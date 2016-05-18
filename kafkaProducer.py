import random
from datetime import datetime
import time
import sys
from kafka import KafkaProducer

class randomProducer():
    def __init__(self):
        self.var = 1
        self.kafkaProd = KafkaProducer()
#
    def runProducer(self):
        try:
            while(self.var==1):
                print "%s I NETWORK  [conn4] end connection 127.0.0.1:36549 (0 connections now open)"%(datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f%z"))
                time.sleep(1+random.random())
        except:
            sys.exit()
#
    def runKafkaProducer(self):
        try:
            while(self.var==1):
                self.kafkaProd.send('first',"%s I NETWORK  [conn4] end connection 127.0.0.1:36549 (0 connections now open)"%(datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f%z")))
                time.sleep(1+random.random())
        except:
            sys.exit()


if __name__ == "__main__":
    a = randomProducer()
    a.runKafkaProducer()
