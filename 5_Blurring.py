# Why it's essential: 
# Blurring is used to reduce noise, smooth images, and sometimes as a preprocessing step for edge detection or other features. 
# Gaussian blur is very common.

import cv2
# Load an image
img = cv2.imread('Vip.jpg')

if img is None:
    print("Error: Could not load image")
else:

     # for resizing the image

    height,width,_ = img.shape

    descale_percent = 10
    new_width = int(width * (descale_percent/100))
    new_height = int(height * (descale_percent/100))

    img = cv2.resize(img, (new_width, new_height))

    # Apply Gaussian Blur

    # cv2.GaussianBlur(src, ksize, sigmaX)
    # ksize: Gaussian kernel size (width, height). Should be positive and odd.
    # sigmaX: Gaussian kernel standard deviation in X direction. If 0, computed from ksize.
    # sigmaY: Gaussian kernel standard deviation in Y direction. Defaults to sigmaX.
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0) # Using a 5x5 kernel

    # You could also try other blur types:
    
    # median_blurred = cv2.medianBlur(img, 5) # Median blur with 5x5 kernel
    # box_blurred = cv2.blur(img, (5, 5)) # Simple box blur with 5x5 kernel


    # Display results
    cv2.imshow('Original', img)
    cv2.imshow('Gaussian Blurred (5x5)', blurred_img)
    # cv2.imshow('Median Blurred (5x5)', median_blurred)

    print("Press any key to close windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()