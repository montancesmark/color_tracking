import cv2
import numpy as np
from color_tracking_modules import color_tracking

def main():

    # Initialize the video capture
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)       #use if device is DirectShow compatible

    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # Define the lower and upper bounds for different colors in HSV
    # Blue
    lower_bound_blue = np.array([100, 150, 50])
    upper_bound_blue = np.array([140, 255, 255])

    # Red (Note: Red wraps around the HSV color wheel, so two ranges are needed)
    lower_bound_red1 = np.array([0, 150, 50])
    upper_bound_red1 = np.array([10, 255, 255])
    lower_bound_red2 = np.array([170, 150, 50])
    upper_bound_red2 = np.array([180, 255, 255])

    # Green
    lower_bound_green = np.array([40, 100, 50])
    upper_bound_green = np.array([80, 255, 255])

    # Yellow
    lower_bound_yellow = np.array([20, 150, 50])
    upper_bound_yellow = np.array([30, 255, 255])

    # NOTE: edit this accordingly
    # Select the color to track (e.g., blue in this example)
    lower_bound = lower_bound_blue
    upper_bound = upper_bound_blue


    while True:
        # Read a frame from the video feed
        ret, frame = cap.read()
        if not ret:
            break

        # Apply color tracking
        mask = color_tracking(frame, lower_bound, upper_bound)

        # For red, combine the two masks
        if lower_bound is lower_bound_red1:
            mask1 = color_tracking(frame, lower_bound_red1, upper_bound_red1)
            mask2 = color_tracking(frame, lower_bound_red2, upper_bound_red2)
            mask = cv2.bitwise_or(mask1, mask2)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw a bounding box around the largest contour
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 500:  # Minimum area threshold
                x, y, w, h = cv2.boundingRect(largest_contour)
                # Calculate average color in the current frame for the bounding box area
                average_color = cv2.mean(frame[y:y+h, x:x+w])[:3]  # Get average BGR color
                cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 255, 255], 3)

        # Display the original frame and the mask
        cv2.imshow('Color Tracking', frame)
        cv2.imshow('Mask', mask)    #just comment this out if not needed

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()