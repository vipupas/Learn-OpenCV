# Why it's essential: 
# Useful for debugging, visualizing object locations (e.g., bounding boxes), annotating images, 
# or creating simple visual outputs.

import cv2
import numpy as np
# Create a black image (or load an image to draw on)
# np.zeros creates a black image (all pixels 0)
# shape: (height, width, channels). 3 channels for color (BGR). dtype=uint8 is standard for images.
blank_image = np.zeros((400, 600, 3), dtype=np.uint8)
img_to_draw = cv2.imread('Vip.jpg').copy() # Use a copy if drawing on loaded image


if img_to_draw is None:
     print("Error: Could not load image. Creating a blank image instead.")
     img_to_draw = blank_image.copy()


# Define colors (BGR format)
blue = (255, 0, 0)    # OpenCV uses BGR not RGB
green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# --- Drawing Shapes ---

# Draw a line: cv2.line(img, start_point, end_point, color, thickness)
cv2.line(img_to_draw, (0, 0), (600, 400), blue, 5)

# Draw a rectangle: cv2.rectangle(img, pt1, pt2, color, thickness)
# pt1: top-left corner, pt2: bottom-right corner
# thickness: positive for outline, -1 or cv2.FILLED for filled rectangle
cv2.rectangle(img_to_draw, (50, 50), (200, 200), green, 3)
cv2.rectangle(img_to_draw, (250, 50), (400, 200), red, cv2.FILLED) # Filled rectangle

# Draw a circle: cv2.circle(img, center, radius, color, thickness)
cv2.circle(img_to_draw, (500, 125), 75, white, -1) # Filled white circle

# --- Drawing Text ---

# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
# org: bottom-left corner of the text string in the image
cv2.putText(img_to_draw, 'Hello, OpenCV!', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Display the result
cv2.imshow('Image with Drawings', img_to_draw)

print("Press any key to close window...")
cv2.waitKey(0)
cv2.destroyAllWindows()
