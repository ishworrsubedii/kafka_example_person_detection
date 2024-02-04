# KAFKA

## KAFKA INSTALLATION FOR LINUX

In this practice project of Kafka, here I have implemented the Kafka producer and consumer for person detection using
YoloV8 and saved the images in a folder and the report in a prediction.txt file from the videos.

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

this is the configuration firle for the kafka broker that will cotain various settings that controls the behaviour of
the kafka broker.

```bash
cd /usr/local/kafka
bin/kafka-server-start.sh config/server.properties
```

## LETS START OUR FIRST KAFKA PRODUCER AND CONSUMER

### Anacond environment
```bash
conda create -n kafka python=3.10
```

```bash
conda activate kafka
```
### Install the requirements

```bash
pip install -r requirements.txt
```
### Run the main file
```bash
python manin.py
```

OR
run manually by the configuration of the root directory of the project.

## Data Flow:

**1. Producer:**

- Receives video, image, or file paths.
- Sends paths to Kafka topics.

**2. Consumer:**

Subscribes to Kafka topics.

- Consumes paths.
- Triggers object detection (using DetectionService) for videos.
- Saves cropped images or prediction results based on configuration.

## Tutorials

- [KAFKA INSTALL](https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-20-04)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



