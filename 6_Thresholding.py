# Why it's essential:
#  Thresholding is a simple yet powerful technique for segmenting an image into two regions (foreground and background) based on pixel intensity.
#  This is often a necessary step before finding contours or other features.

import cv2
# Load an image in grayscale (thresholding is typically done on grayscale)
img_gray = cv2.imread('Vip.jpg', 0)

if img_gray is None:
    print("Error: Could not load image.")
else:

     # for resizing the image

    height,width= img_gray.shape # grayscale give two parameter

    descale_percent = 10
    new_width = int(width * (descale_percent/100))
    new_height = int(height * (descale_percent/100))

    img_gray = cv2.resize(img_gray, (new_width, new_height))

    # Apply simple binary thresholding
    # cv2.threshold(src, thresh, maxval, type)
    # src: Input grayscale image (NumPy array)
    # thresh: Threshold value
    # maxval: Maximum value to use with binary types
    # type: Thresholding type (e.g., cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TOZERO, etc.)

    # If pixel intensity > thresh, set to maxval (255). Otherwise, set to 0.
    thresh_value = 127
    max_value = 255
    ret, binary_thresholded = cv2.threshold(img_gray, thresh_value, max_value, cv2.THRESH_BINARY)

    # ret is the actual threshold value used (useful for Otsu's method, not simple thresholding)

    # Inverse binary thresholding: If pixel intensity > thresh, set to 0. Otherwise, set to maxval.
    ret_inv, binary_inv_thresholded = cv2.threshold(img_gray, thresh_value, max_value, cv2.THRESH_BINARY_INV)


    # Display results
    cv2.imshow('Grayscale', img_gray)
    cv2.imshow('Binary Thresholded (Thresh=127)', binary_thresholded)
    cv2.imshow('Binary Inverse Thresholded (Thresh=127)', binary_inv_thresholded)

    print("Press any key to close windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()