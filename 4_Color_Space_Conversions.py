# Why it's essential:
# Different color spaces are useful for different tasks. 
# Grayscale simplifies processing. 
# HSV (Hue, Saturation, Value) is often better for color-based segmentation than BGR because Hue is less sensitive to lighting changes.


import cv2

# load an image 
img = cv2.imread('Vip.jpg')



if img is None:
    print("Error : image not found")
else:

    # for resizing the image

    height,width,_ = img.shape

    descale_percent = 10
    new_width = int(width * (descale_percent/100))
    new_height = int(height * (descale_percent/100))

    img = cv2.resize(img, (new_width, new_height))

    # Convert BGR to Grayscale
    gray_img = cv2. cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Convert BGR to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Convert BGR to LAB
    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)


    # Display results
    cv2.imshow('Original (BGR)', img)
    cv2.imshow('Grayscale',gray_img)
    cv2.imshow('HSV',hsv_img)
    # Note: HSV channels look different when displayed directly as an image

    # displaying the Hue channel might be more informative
    cv2.imshow('HSV - Hue Channel',hsv_img[:,:,0])
    print('press any key to close windows...')
    cv2.waitKey(0)
    cv2.destroyAllWindows()

 