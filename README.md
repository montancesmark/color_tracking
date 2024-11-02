![image](https://github.com/user-attachments/assets/ef91a107-12a3-499a-9abc-76c7d440199a)

# Color Tracking Project

This project implements a real-time color tracking application using OpenCV and Python. 
The application captures video from a camera, processes each frame to detect specified colors, and draws bounding boxes around the detected objects.

## Features

- Real-time color detection for various colors (Red, Green, Blue, Yellow).
- Dynamic bounding box color that matches the detected object.
- Contour detection to identify and track the largest colored object in the frame.
- Morphological operations to enhance mask quality by removing noise.

## Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the required packages using pip:

pip install opencv-python numpy


## Usage

Clone the repository:

git clone https://github.com/montancesmark/color_tracking.git

cd color-tracking


Run the color tracking script:

python color_tracking.py

Ensure your camera is connected and accessible. 
The application will open a window displaying the live video feed and the mask for the detected colors.

Press 'q' to exit the application.

## Color Tracking
The default color tracking is set to Blue, but you can easily modify the lower and upper HSV bounds in the script to track other colors as needed:

Red:
Lower Bound: [0, 150, 50], [170, 150, 50]
Upper Bound: [10, 255, 255], [180, 255, 255]

Green:
Lower Bound: [40, 100, 50]
Upper Bound: [80, 255, 255]

Yellow:
Lower Bound: [20, 150, 50]
Upper Bound: [30, 255, 255]

## License
This project is licensed under the MIT License. 

