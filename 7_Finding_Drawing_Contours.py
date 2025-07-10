# ✨ A contour is just a line that goes around the shape of an object.
# They help the computer understand what’s in a picture.
# They’re useful to find, detect, recognize, and follow objects.
# Without contours, a computer would just see millions of dots and go 😵‍💫.

import cv2

# Load an image
img = cv2.imread('Vip.jpg')

if img is None:
    print("Error: Could not load image .")
else:
    # --- Preprocessing for Contours ---
    # Contours are typically found on binary images.
    # 1. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 2. Apply thresholding (or Canny edge detection is another common approach)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV) # Inverse for black object on white background example

    # Make a copy of the image to draw on
    img_contours = img.copy()

    # --- Finding Contours ---
    # cv2.findContours(image, mode, method)
    # image: Source binary image (8-bit single channel)
    # mode: Contour retrieval mode (e.g., cv2.RETR_EXTERNAL for outer contours, cv2.RETR_LIST for all)
    # method: Contour approximation method (e.g., cv2.CHAIN_APPROX_SIMPLE to compress horizontal/vertical/diagonal segments)

    # Note: findContours modifies the input image in some OpenCV versions.
    # Use a copy of the thresholded image if you need the original binary image later.
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # --- Drawing Contours ---
    # cv2.drawContours(image, contours, contourIdx, color, thickness)
    # image: Image to draw on (can be color or grayscale)
    # contours: List of contours (output from findContours)
    # contourIdx: Index of the contour to draw (-1 to draw all)
    # color: Color of the contour (BGR tuple)
    # thickness: Thickness of the contour line (negative value like cv2.FILLED to fill the contour)

    # Draw all contours in green with thickness 2
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

    print(f"Found {len(contours)} contours.")

    # Display results
    cv2.imshow('Original', img)
    cv2.imshow('Thresholded (for contours)', thresh)
    cv2.imshow('Contours', img_contours)

    print("Press any key to close windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()