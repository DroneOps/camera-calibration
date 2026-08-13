# camera-calibration

Camera calibration toolkit for working with chessboard images. It can capture frames from a local webcam or a DJI Tello drone, detect the inner chessboard corners, and use those points to estimate the camera calibration matrix.

## How it works
1. Capture images of a chessboard pattern using either your webcam or a DJI Tello drone.
2. Run the calibration script to detect obtain the camera calibration matrix.

## Requirements

```bash
pip install opencv-python numpy djitellopy
```

## Capture from webcam

The script *captureImage.py* is used to capture images from a webcam.

- Press `s` to save an image.
- Press `q` to exit.

By default, it uses camera index `0`:

```python
cap = cv.VideoCapture(0)
```

If your webcam is mapped to another index, change that value.

## Capture from DJI Tello

The script *telloImage.py* is used to capture images from a DJI Tello drone. As it uses the captureImage.py script, the same key bindings apply.

## Calibration script

The script *getCalibrationMatrix.py* is used to compute the camera calibration matrix.

- Loads all `.jpg` images in the project folder. You can change the image format in the script if needed.
- Looks for the 13x10 squares by default. But you can change the inner-corner count in the script if your chessboard has a different size.

If `findChessboardCorners` cannot detect the pattern:

- make sure the inner-corner count is correct
- use good lighting
- keep the board fully visible in the image
- avoid blur and strong reflections
- capture images from different angles

**Note:** The calibration matrix in this repo is for the djitello camera, but you can use your own images to compute a new calibration matrix.

