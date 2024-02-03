# KAFKA

## KAFKA INSTALLATION FOR LINUX

### Step 1: Download the Kafka

- Download the Kafka from the official website of Apache Kafka.
- [Apache Kafka](https://kafka.apache.org/downloads)

OR

```bash
wget https://downloads.apache.org/kafka/3.6.1/kafka_2.12-3.6.1.tgz
```
### Step 2: Extract the Kafka

```bash
tar -xzf kafka_2.12-3.6.1.tgz
```

### Step 3: Move the Kafka to the /usr/local directory

```bash
sudo mv kafka_2.12-3.6.1 /usr/local/kafka
```

### Step 4: Start the Zookeeper
this will start the zookeeper server which helps to manage the large set of the host .

```bash
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Step 5: Start the Kafka Server
this is the configuration firle for the kafka broker that will cotain various settings that controls the behaviour of the kafka broker.
```bash
cd /usr/local/kafka
bin/kafka-server-start.sh config/server.properties
```
## LETS START OUR FIRST KAFKA PRODUCER AND CONSUMER

python main.py

```


