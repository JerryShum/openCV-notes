import cv2 as cv

# contour sikmilar as edges but not same as mathematically
# for shape analysis and object recognition

img = cv.imread('Photos/cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

thresholding_type = cv.THRESH_BINARY
ret, thresh = cv.threshold(gray, 125, 255, thresholding_type)
cv.imshow('Thresh', thresh)

# blur = cv.GaussianBlur(thresh, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# mode = cv.RETR_TREE # returns all hierarchial contours (only in a hierarchial system)
# mode = cv.RETR_EXTERNAL # retrieves only external contours (outside)
mode = cv.RETR_LIST # a method of finding contours - finds all contours in image and 
contours, hierarchies = cv.findContours(thresh, mode, cv.CHAIN_APPROX_NONE)

print(len(contours))

# chain_approx_none == get all contours points
# chain_approx_simple == get all poionts of line, compresses it into two end poitns only

# contours == list of points of all contours
# hierarchies == representation that open cv uses to find contours inside of other contours



cv.waitKey(0)

# USE GREYSCALE FOR BTOH
# BLUR ONLY USED WITH CANNY
# THRESHOLD used alone