import cv2
import numpy as np

class YOLODetector:
    def __init__(self, confidence_threshold=0.5):
        self.confidence_threshold = confidence_threshold
        self.nms_threshold = 0.3

        self.net = cv2.dnn.readNet("yolo/yolov4.weights", "yolo/yolov4.cfg")
        self.layer_names = self.net.getUnconnectedOutLayersNames()
        self.classes = self.load_classes("yolo/coco.names")

    def load_classes(self, class_file):
        with open(class_file, "r") as f:
            return [line.strip() for line in f.readlines()]

    def detect_people(self, frame):
        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        detections = self.net.forward(self.layer_names)

        boxes = []
        confidences = []
        # Wir sammeln alle Boxen und deren Konfidenzwerte
        for output in detections:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > self.confidence_threshold and self.classes[class_id] == "person":
                    box = detection[0:4] * np.array([width, height, width, height])
                    (centerX, centerY, w, h) = box.astype("int")
                    x = int(centerX - (w / 2))
                    y = int(centerY - (h / 2))
                    boxes.append([x, y, int(w), int(h)])
                    confidences.append(float(confidence))


        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, self.nms_threshold)
        people_detected = False
        if len(indices) > 0:
            for i in indices.flatten():
                people_detected = True
                (x, y, w, h) = boxes[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)  # Rote Box, 3 Pixel dick
                cv2.putText(frame, f"Person {confidences[i]:.2f}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        return people_detected


class YOLODetectorWithFrameSkipping:
    def __init__(self, confidence_threshold=0.5, frame_skip=10):
        self.detector = YOLODetector(confidence_threshold)
        self.frame_skip = frame_skip
        self.frame_count = 0

    def process_frame(self, frame):
        self.frame_count += 1
        if self.frame_count % self.frame_skip == 0:
            people_detected = self.detector.detect_people(frame)
        else:
            people_detected = False
        return people_detected
