import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Cat', img)

# 1. Convert image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur = remove noise (e.g. bad lighting, isseus with camera sensor)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
# increase kernel size to increase blur

# 3. Edge Cascade, find edges present in the image
threshold1 = 125
threshold2 = 175
canny = cv.Canny(img, threshold1, threshold2)
cv.imshow('Canny', canny)


# 3a. Edge CAscade but pass in blur
cannyBlur = cv.Canny(blur, threshold1, threshold2)
cv.imshow('Canny Blur', cannyBlur)

# 4 Dilate 

dilated = cv.dilate(cannyBlur, (7, 7), iterations=5)
cv.imshow('Dilated', dilated)

# 5 Eroded
eroded = cv.erode(dilated, (7, 7), iterations=5)
cv.imshow('Eroded', eroded)

# erode is inverse of dilation

# Rsize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) # interpolation = INTER_AREA, best for scaling down, INTER_LINEAR best for upscaling or INTER_CUBIC (slowest, but higher quality)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 100:200]
cv.imshow('Cropped', cropped)

cv.waitKey(0)