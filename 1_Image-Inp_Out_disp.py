# Why it's essential:
#  Every image processing task starts with loading an image, and you need to see the results.
#  Saving is crucial for output.


import cv2
# Read an image
# cv2.imread(filename,flag)
# flag = 1 :Color image (default)
# flag = 0 :Grayscale image 
# flag = -1:Unchanged (including alpha channel if present)

img_color = cv2.imread("Vip.jpg",1)
img_gray = cv2.imread("Vip.jpg",0)

# check if image loaded or not 
if img_color is None:
    print("Error : image is not loaded")
else:

    # Display image 
    # cv2.imshow(window_name, image)
    cv2.imshow("Color Image", img_color)
    cv2.imshow("GrayScale Image", img_gray)


    # wait for a key press 
    # cv2.waitKey(delay_ms)
    # 0 meand wait for indefinitely

    # without this it run and close the window 

    print("press any key to close windows ... ")
    cv2.waitKey(0)

    # Save the image 
    # cv2.imwrite(filename,image)

    cv2.imwrite('gray_vip.jpg',img_gray)


    # Destroy all opencv windows

    cv2.destroyAllWindows()