from kafka import KafkaProducer
import json


class VideoPathProducer:
    def __init__(self, bootstrap_servers, topic_name):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.topic_name = topic_name

    def send_video_path(self, video_path):
        """
        Send the video path to the Kafka topic
        :param video_path:  video path to be passed
        :return:  None
        """
        self.producer.send(self.topic_name, video_path)
        self.producer.flush()

    def send_file_path(self, file_path):
        """
        Send the file path to the Kafka topic
        :param file_path:  file path to be passed
        :return: None
        """
        self.producer.send(self.topic_name, file_path)
        self.producer.flush()

    def send_image_save(self, image_path):
        """
        Send the image path to the Kafka topic
        :param image_path:  image path to be passed
        :return:  None
        """
        self.producer.send(self.topic_name, image_path)
        self.producer.flush()
