from src.kafka_pipeline.kafka_producer import VideoPathProducer
from src.kafka_pipeline.kafka_consumer import VideoPathConsumer
from src.kafka_pipeline.object_detection import DetectionService


def main():
    bootstrap_servers = 'localhost:9092'
    topic_name = 'video_paths'
    group_id = 'group1'
    model_path = 'resources/model/yolov8n.pt'

    detection_service = DetectionService(model_path)
    producer = VideoPathProducer(bootstrap_servers, topic_name)
    consumer = VideoPathConsumer(bootstrap_servers, topic_name, group_id, detection_service)

    video_path = 'resources/videos/People Walking Free Stock Footage, Royalty-Free No Copyright Content.mp4'
    file_path = 'reports/prediction.txt'
    save_image_path = 'resources/images/'
    producer.send_video_path(video_path)
    producer.send_file_path(file_path)
    producer.send_image_save(save_image_path)

    consumer.consume_video_path(save_image_path=True, save_pred_info=True)



if __name__ == "__main__":
    main()
