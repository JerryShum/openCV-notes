import cv2 as cv

#! Reading Images

# # Takes image and returns matrix of pixels
# img = cv.imread('Photos/cat_large.jpg')

# # Displays image as a window, 2 parameters: name of window AND matrix of image
# cv.imshow('Cat', img)

#! Reading Videos
# Takes in integer values, 0 = webcam, 1 = first camera connected, 2 = 2nd camera, etc.
capture = cv.VideoCapture('Videos/dog.mp4')

# Loop to read video (Reads frame by frame)
while True:
    # returns frames, 
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    # if d is pressed, break
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
    # read frame -> wait 20 ms, 
    

capture.release()
cv.destroyAllWindows()

# -215 insertion failed error code (location is wrong) -> video ran out of frames -> breaks out of while loop


# Waits for keyboard input,
cv.waitKey(0)