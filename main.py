from flask import Flask, render_template, Response, jsonify, request, session
import cv2
import time
from motion_detector import MotionDetector

app = Flask(__name__)
app.secret_key = 'secret_key'
camera = cv2.VideoCapture(0)
motion_detector = MotionDetector()
motion_log = []

def get_available_cameras():
    available_cameras = []
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
        cap.release()
    return available_cameras

available_cameras = get_available_cameras()
print(f"Verfügbare Kameras: {available_cameras}")

def change_camera(camera_index):
    global camera
    camera.release()
    camera = cv2.VideoCapture(camera_index)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        motion_detected = motion_detector.detect_motion(frame)

        if motion_detected:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            motion_log.append(f"Bewegung erkannt um {timestamp}")
            print(f"🔴 Bewegung erkannt um {timestamp}")

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    if 'last_access' in session:
        session['last_access'] = time.time()
    else:
        session['last_access'] = time.time()

    available_cameras = get_available_cameras()  # Liste verfügbarer Kameras
    return render_template('index.html', last_access=session['last_access'], cameras=available_cameras)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/motion_log')
def get_motion_log():
    return jsonify(motion_log)

recording = False

@app.route('/toggle_recording', methods=['POST'])
def toggle_recording():
    global recording
    recording = not recording
    return jsonify({"recording": recording})

# Route zum Wechseln der Kamera
@app.route('/switch_camera', methods=['POST'])
def switch_camera():
    camera_index = int(request.form['camera_index'])
    change_camera(camera_index)
    return jsonify({"camera_index": camera_index})

if __name__ == '__main__':
    app.run(debug=True)
