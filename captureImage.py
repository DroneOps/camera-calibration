'''
A simple script to capture an image from the webcam and save it to a file.
'''

import cv2 as cv
import time
import os
printed = False

def fileCounter(name, counter, extension):
    file = f"{name}{counter}.{extension}"
    return file
    

def captureImage(frame):
    global printed
    if not printed:
        print("Press 's' to save the image")
        print("Press 'q' to exit")
        printed = True
    
    # if the frame is read correctly, we show the image and wait for a key press to save it to a file
    
    cv.imshow('image', frame)
    key = cv.waitKey(1) & 0xFF

    '''Saving images'''
    if key == ord('s'):
        print("Capturing image")
        imageName = "Chessboard"
        imageCounter = 0
        imageExtension = "jpg"
        file = fileCounter(imageName,imageCounter, imageExtension)
        while(os.path.exists(file)):
            imageCounter += 1
            file = fileCounter(imageName,imageCounter, imageExtension)

        success = cv.imwrite(file, frame) 
        if(success):
            print("----")
            print(f"Done saved as {file} ")
            print("----")
            time.sleep(3)
        else:
            print("Error: could not save the image")

    elif key == ord('q'):
        return False      

    return True      


def main():
    cap = cv.VideoCapture(0)


    while 1:
        ret, frame = cap.read()
        if not ret:
            break
        
        quit = captureImage(frame)
        if not quit:
            break 

    cap.release()

if __name__ == "__main__":
    main()