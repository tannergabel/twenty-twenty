import cv2
from cv2 import VideoCapture

from eye import EyeTracker

ESC_ASCII_CODE = 27
FRAME_INTERVAL_IN_MS = 500

def process_frame(frame):
    tracker = EyeTracker()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("No camera detected.")
    exit()

while True:
    camera.grab()
    status, frame = camera.retrieve()

    if status:
        process_frame(frame)
    else:
        print("Could not get image")
    
    c = cv2.waitKey(FRAME_INTERVAL_IN_MS)
    if c == ESC_ASCII_CODE:
        break

camera.release()
cv2.destroyAllWindows()