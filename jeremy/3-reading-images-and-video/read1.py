import cv2 as cv

# cv.imread('') # takes image and returns matrix of pixels
img = cv.imread('Photos/cat_large.jpg') # img holds 

cv.imshow('Cat', img) # displays image as a window. 2 parameters: name of window AND matrix of pixels to display

cv.waitKey(0) # keyboard binding function. waits for time in milliseconds delay (0 = infinite of tiem for keyboard key to be pressed)


