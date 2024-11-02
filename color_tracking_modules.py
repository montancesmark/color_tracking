import cv2
import numpy as np

# Function to create a mask for the specified color range
def color_tracking(frame, lower_bound, upper_bound):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the given color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Perform morphological operations to remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    return mask