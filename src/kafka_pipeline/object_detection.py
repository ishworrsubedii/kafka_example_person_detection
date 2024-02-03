import cv2
from ultralytics import YOLO


class DetectionService:
    def __init__(self, model_path: str):
        self.model_instance = YOLO(model_path)

    def detect_video(self, video_path: str, confidence_threshold: float, nms_threshold: float):
        """
        Detects vehicle number plates from a video in real-time and yields detections one at a time
        :param video_path:  video path to be passed
        :param confidence_threshold:  confidence threshold
        :param nms_threshold: nms threshold
        :yield: Tuple with prediction and cropped frame for each detection
        """
        cap = cv2.VideoCapture(video_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame")
                break
            frame = cv2.resize(frame, (640, 480))  # Resize the frame
            results = self.model_instance(frame, conf=confidence_threshold, iou=nms_threshold)
            for prediction in results:
                bboxes = prediction.boxes.xyxy
                try:
                    bbox = bboxes[0].int().tolist()
                    x1, y1, x2, y2 = bbox
                    cropped = frame[y1:y2, x1:x2]
                    yield (prediction, cropped)
                except Exception as e:
                    print(e)
        cap.release()
