# camera-calibration

Camera calibration toolkit for working with chessboard images. It can capture frames from a local webcam or a DJI Tello drone, detect the inner chessboard corners, and use those points to estimate the camera calibration matrix.

## What this project does

1. Capture an image of the chessboard.
2. Save this image in the project folder.
3. Run the calibration script to detect the inner corners.
4. Use the detected points to compute the camera calibration matrix.

## Requirements

```bash
pip install opencv-python numpy djitellopy
```

## Capture from webcam

The script captureImage.py 

1. Open a window showing the webcam feed.
2. Press `s` to save an image.
3. Press `q` to exit.

By default, it uses camera index `0`:

```python
cap = cv.VideoCapture(0)
```

If your webcam is mapped to another index, change that value.

## Capture from DJI Tello

The script telloImage.py

1. Connect to the drone.
2. Read and print the battery level.
3. Start the video stream.
4. Display each frame.
5. Press `s` to save an image.
6. Press `q` to exit.
7. Turn off the stream when finished.

## Calibration script

The script getCalibrationMatrix.py

1. Loads all `.jpg` images in the project folder.
2. Detects the inner corners of the chessboard pattern.
3. Show the detected corners in a window.
4. Wait for a key press to continue.
5. After processing the image, it computes the camera calibration matrix prints it to the console.
6. Saves the calibration matrix to a file named `calibration_matrix.txt`.

If `findChessboardCorners` cannot detect the pattern:

- make sure the inner-corner count is correct
- use good lighting
- keep the board fully visible in the image
- avoid blur and strong reflections
- capture images from different angles

The calibration matrix in this repo is for the djitello camera, but you can use your own images to compute a new calibration matrix.

