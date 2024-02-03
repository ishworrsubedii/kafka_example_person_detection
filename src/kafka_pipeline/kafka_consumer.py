import datetime

from kafka import KafkaConsumer
import json
import cv2


class VideoPathConsumer:
    def __init__(self, bootstrap_servers, topic_name, group_id, detection_service):
        self.consumer = KafkaConsumer(topic_name,
                                      bootstrap_servers=bootstrap_servers,
                                      group_id=group_id,
                                      value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        self.detection_service = detection_service

    def consume_file_path(self, predictions):
        for message in self.consumer:
            file_path = message.value
            with open(file_path, 'w') as file:
                for prediction in predictions:
                    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    file.write(f'{current_time}\t{str(prediction[0])}\n')  # Write the prediction value to the file

    def consume_image_save(self, predictions):
        for message in self.consumer:
            image_path = message.value
            for prediction in predictions:
                cropped = prediction[1]
                current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                cv2.imwrite(f'{image_path}/{current_time}.jpg', cropped)

    def consume_video_path(self, save_image_path: bool, save_pred_info: bool):
        for message in self.consumer:
            video_path = message.value
            for prediction in self.detection_service.detect_video(video_path, confidence_threshold=0.5,
                                                                  nms_threshold=0.5):
                print(f"Prediction: {prediction}")
                if save_image_path:
                    self.consume_image_save([prediction])
                if save_pred_info:
                    self.consume_file_path([prediction])

