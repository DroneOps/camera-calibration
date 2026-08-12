'''
This script uses the capture_image.py to capture an image from the djitello camera
'''
import os


import cv2 as cv
import time
from djitellopy import Tello


tello = Tello()


tello.connect()

battery = tello.get_battery()

print(f"Conected battery at {battery} %")
tello.streamon()


time.sleep(2)

cap = tello.get_frame_read()


while 1:
    image = cap.frame
   
    cv.imshow("Image", image)


    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

tello.streamoff()
cv.destroyAllWindows()
    
