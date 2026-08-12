'''
A simple script to get the calibration matrix from a set of images of a chessboard pattern.
You can see the full tutorial here: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
'''

import numpy as np
import cv2 as cv
import glob


#Chessboard size, number of squares.
#if your chessboard has 13x10 counting the squares putting chessboard in vertical position.
num_rows = 13 # change this to match yours
num_cols = 10 # change this to match yours
chessboard_size = (num_rows - 1, num_cols - 1) # we subtract 1 because the number of inner corners is one less than the number of squares

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboard_size[0]*chessboard_size[1],3), np.float32)
objp[:,:2] = np.mgrid[0:chessboard_size[1],0:chessboard_size[0]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.jpg')


for fname in images:
    print("Image Found")
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, chessboard_size, None) 

    print(f"Chessboard corners found: {ret}")

    if ret == True:
        print("Getting Calibration Matrix")
        objpoints.append(objp)

        corners2 = cv.cornerSubPix(gray,corners, chessboard_size, (-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners

        print("Showing chessboard, press any key to exit")
        cv.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(0)

cv.destroyAllWindows()

print("Calibration Matrix:")
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(ret, mtx, dist, rvecs, tvecs)

with open('calibration_matrix.txt', 'w') as f:
    f.write(f"ret: {ret}\n")
    f.write(f"mtx: {mtx}\n")
    f.write(f"dist: {dist}\n")
    f.write(f"rvecs: {rvecs}\n")
    f.write(f"tvecs: {tvecs}\n")



