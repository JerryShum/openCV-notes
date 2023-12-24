import cv2 as cv

img = cv.imread('../Content/Resources/Photos/park.jpg')
cv.imshow('Park', img)

# ---

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# ---
# Blur
# Remove noise in image

# Gaussian
# (canvas, kernelsize = strength of blur, sodjasdlkjasdlkajsdlaksdjalskd)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# ---
# Edge Cascade
# Outline edges inside of image

# canny -> technique of finding edges in an image
canny = cv.Canny(blur,125,175)
cv.imshow("Canny Edges", canny)

# Finds the edges inside of an image and displays it all in black and white
# Pass in blur to sort for really strong edges
# Pass in different blur values to find different types of edges

# ---
# Dilate Images
# Emphasize Edges
# Based on structural elements

dilated = cv.dilate(canny, (7,7), iterations=5)
cv.imshow("Dilated", dilated)

# ---
# Erode Images
# Reverse Dilation

eroded = cv.erode(dilated, (7,7), iterations=5)
cv.imshow('Eroded', eroded)

# ---
# Resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
# [y,x]
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

# ---

cv.waitKey(0)