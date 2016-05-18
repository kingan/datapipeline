# datapipeline
This project focused on the setup and configuration of a data pipeline consisting of Kafka, Spark, and MongoDB.

https://github.com/kingan/datapipeline


Setup Kafka

Initial Kafka Setup

Download the tarball file
	http://ftp.heanet.ie/mirrors/www.apache.org/dist/kafka/0.9.0.1/kafka-0.9.0.1-src.tgz
Create the log directories
	/usr/local/kafka/logs/kafka_logs_1
Adjust the configuration file
	/usr/local/kafka/config/server1.properties. 
Launch zookeeper
	bin/zookeeper-server-start.sh config/zookeeper.properties &
Launch kafka server
bin/kafka-server-start.sh config/server1.properties &

Create a kafka topic

	bin/kafka-topics.sh --zookeeper localhost:2181 --create --partitions 2 --replication-factor 2 --name first


Write Python Producer and Consumer

https://github.com/kingan/datapipeline/blob/master/kafkaProducer.py
https://github.com/kingan/datapipeline/blob/master/kafkaConsumer.py


Setup MongoDB

	mongod --config /etc/conf/datapipeline.conf



