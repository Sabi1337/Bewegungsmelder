import cv2
import os
import time
import requests
from yolo_detector import YOLODetector


class MotionDetector:

    def __init__(self, min_area=8000, blur_size=(25, 25), threshold_value=30):
        self.camera = cv2.VideoCapture(0)
        self.first_frame = None
        self.is_recording = False
        self.video_writer = None
        self.last_motion_time = None
        self.min_area = min_area
        self.blur_size = blur_size
        self.threshold_value = threshold_value
        self.TELEGRAM_BOT_TOKEN = "7895698771:AAF_VIwnPrFQ57GzC1lkKWa59uIBzO89_Ho"
        self.TELEGRAM_CHAT_ID = "7824475671"
        self.last_telegram_time = 0
        self.yolo = YOLODetector()
        os.makedirs("videos", exist_ok=True)

    def send_telegram_alert(self, message):
        if time.time() - self.last_telegram_time < 60:
            return
        url = f"https://api.telegram.org/bot{self.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": self.TELEGRAM_CHAT_ID, "text": message}
        response = requests.post(url, json=payload)
        print("Telegram response:", response.text)
        self.last_telegram_time = time.time()

    def detect_motion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, self.blur_size, 0)

        if self.first_frame is None:
            self.first_frame = gray
            return False

        frame_delta = cv2.absdiff(self.first_frame, gray)
        thresh = cv2.threshold(frame_delta, self.threshold_value, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = any(cv2.contourArea(c) > self.min_area for c in contours)

        person_detected = self.yolo.detect_people(frame)

        if motion_detected and person_detected:
            self.send_telegram_alert(f"🚨 Person erkannt um {time.strftime('%Y-%m-%d %H:%M:%S')}.Hier ist deine Ngrok-URL: https://e682-2a02-8071-51c0-7940-b0df-1929-89f4-3c20.ngrok-free.app.")
            if not self.is_recording:
                self.start_recording(frame)
            self.last_motion_time = time.time()
        elif self.is_recording and self.last_motion_time and time.time() - self.last_motion_time > 3:
            self.stop_recording()

        if self.is_recording:
            self.video_writer.write(frame)

        self.first_frame = cv2.addWeighted(self.first_frame, 0.9, gray, 0.1, 0)

        return motion_detected

    def start_recording(self, frame):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        video_filename = f"videos/motion_{timestamp}.avi"
        height, width, _ = frame.shape
        self.video_writer = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))
        self.is_recording = True
        print(f"🎥 Aufnahme gestartet: {video_filename}")

    def stop_recording(self):
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
        self.is_recording = False
        print("🛑 Aufnahme gestoppt")
