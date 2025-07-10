# Why it's essential: 
# Images often need to be standardized in size (e.g., for network input) 
# or focused on a specific region of interest (ROI).

import cv2
# Load an image
img = cv2.imread("Vip.jpg")

if img is None:
    print("Error : image is not loaded ")
else:
    # Get original dimentions
    height,width,_ = img.shape
    print(f"Orignal Dimensions: {width}x{height}")

    # --- Resizing ---
    # cv2.resize(src,dsize,fx,fy,interpolation)
    # dsize: desired size (width,height) - can be None if fx/fy are used
    # fx,fy: scaling factors along x and y axes
    # interpolation: method used
    #(e.g. cv2.INTER_AREA for shrinking, cv2.INTER_CUBIC or cv2.INTER_LINEAR for zooming)

    resized_fixed = cv2.resize(img,(300,200))
    print(f"Resized (fixed size)Dimensions: {resized_fixed.shape[1]}x{resized_fixed.shape[0]}")

    # Resize by a scaling factor (e.g., 50%)
    scale_percent = 50
    new_width = int(width * scale_percent/100)
    new_height = int(height * scale_percent/100)

    resized_scaled = cv2.resize(img, (new_width, new_height))
    print(f"Resized (scales) Dimensions: {resized_scaled.shape[1]}x{resized_scaled.shape[0]}")

    # --- Cropping ---
    # Cropping is done using NumPy slicing: image[startY:endY,startX:endX]
    # Let's crop the top-left quarter of the image 
    start_row, start_col = int(height * 0.25), int(width * 0.25)
    end_row, end_col = int(height * 0.75), int(width * 0.75)
    cropped_img = img[start_row:end_row, start_col:end_col]
    print(f"Cropped Dimensions: {cropped_img.shape[1]}x{cropped_img.shape[0]}")


    # Display results
    cv2.imshow('Original',img)
    cv2.imshow('Resized (Fixed 300x200)',resized_fixed)
    cv2.imshow('Resized (Scaled 50%)', resized_scaled)
    cv2.imshow('Cropped (Center 50%)',cropped_img)

    print('press any key to close windows...')
    cv2.waitKey(0)
    cv2.destroyAllWindows()