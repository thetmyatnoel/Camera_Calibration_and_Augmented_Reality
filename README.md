# Camera_Calibration_and_Augmented_Reality_with_Chessboard

This program demonstrates camera calibration, Perspective-n-Point (PnP) pose estimation, and Augmented Reality (AR) rendering using a chessboard pattern. The program first calibrates the camera by analyzing a video containing various viewpoints of the chessboard. Next, it tests the PnP algorithm and renders a simple 3D pyramid on the detected chessboard.


## Features
1. Camera calibration using chessboard pattern
2. PnP pose estimation
3. AR rendering of a 3D pyramid


## Requirements
1. Python 3
2. OpenCV

## Usage

1. Record a video of a chessboard pattern being observed from various viewpoints. Make sure the chessboard pattern has a known size and number of inner corners (e.g., 10x7).

2. Update the input_file variable in the code with the path to your recorded chessboard video.

3. Set the board_pattern variable to the number of inner corners of your chessboard (e.g., (10, 7)).

4. Set the board_cellsize variable to the size of a single cell in your chessboard (e.g., 0.025 for 25mm).

5. Run the program. The camera will be calibrated, and the estimated camera matrix and distortion coefficients will be displayed.

6. The program will then use the PnP algorithm to estimate the camera pose in each frame of the video and render a 3D pyramid on the detected chessboard.

## Acknowledgements
This program is based on the OpenCV library and its functions for camera calibration, PnP pose estimation, and 2D/3D point projection.

## Camera Calibration Results
* The number of selected images = 30
* RMS error = 0.5930317199415904
* Camera matrix (K) = 
[[1.65450289e+03, 0.00000000e+00, 9.64907984e+02],
 [0.00000000e+00, 1.65798710e+03, 5.36056186e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]
* Distortion coefficient (k1, k2, p1, p2, k3, ...) = [ 3.37401908e-01, -2.22725768e+00,  1.79713514e-03, -7.08231523e-04,
  4.80412419e+00]
