import cv2
import time
import traceback
from picamera2 import Picamera2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class VideoCamera:
    def __init__(self):
        try:
            # Initialize Picamera2 and configure it
            self.picam2 = Picamera2()
            preview_config = self.picam2.create_preview_configuration(main={"format": "XRGB8888", "size": (640, 480)})
            self.picam2.configure(preview_config)
            self.picam2.start()
            time.sleep(1)  # Allow time for the camera to start
        except Exception as e:
            print(f"Error initializing camera: {e}")
            self.picam2 = None

    def __del__(self):
        if self.picam2:
            self.picam2.stop()

    def get_frame(self):
        if self.picam2:
            try:
                # Capture frame as numpy array
                frame = self.picam2.capture_array()
                # Convert to BGR color (OpenCV default)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                _, jpeg = cv2.imencode('.jpg', frame)
                return jpeg.tobytes()
            except Exception as e:
                print(f"Error capturing frame: {e}")
                return None
        return None


def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    # Create the camera instance and stream the frames
    camera = VideoCamera()
    return StreamingHttpResponse(gen(camera), content_type='multipart/x-mixed-replace; boundary=frame')