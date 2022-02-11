import cv2
from cv2 import VideoCapture

ESC_ASCII_CODE = 27

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("No camera detected.")
    exit()

while True:
    camera.grab()
    status, frame = camera.retrieve()

    if status:
        cv2.imshow("Video", frame)
    else:
        print("Could not get image")
    
    c = cv2.waitKey(1)
    if c == ESC_ASCII_CODE:
        break

camera.release()
cv2.destroyAllWindows()