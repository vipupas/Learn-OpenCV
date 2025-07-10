# Why it's essential:
#  Processing live camera feeds or video files is fundamental to many dynamic vision tasks (tracking, surveillance, etc.).

import cv2

# Replace 0 with the path to a video file (e.g 'myvdo.mp4')
# 0 typically refers to the default camera ( which is build in )
cap = cv2.VideoCapture(0)

# Check if camera / video file opened or not 
if not cap.isOpened():
    print("Error : video source not found ")
    exit()

print("press 'q' to exit the video feed ")


while(True):
    # Read a frame form the video capture object 
    # cap.read()  returns a tuple : ( ret , frame)
    # ret is True if the frame was read successfully, False otherwise
    # frame is the image frame  ( a numpy array )
    ret,frame = cap.read()

    #If frame is not read correctly, break the loop
    if not ret:
        print(" cant receive frame (stream end ??). Exiting ... ")
        break


    # --- now perform operations on the frame here ---
    # for example converting  the to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    # Display  the resulting frame
    cv2.imshow('Original Frame',frame)
    cv2.imshow('Grayscale Frame', gray_frame)


    # Break the loop if 'q' is pressed
    # cv2.waitKey(1) wait for 1 millisecond. this is crucial for video processing
    # 0xFF is a bitmask to get the lowest 8 bits , needed for compatibility across systems
    # 0xFF = 11111111
    # ord('q') == 113
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture video and destroy windows
cap.release()
cv2.destroyAllWindows()