import cv2 as cv
import numpy as np

img = cv.imread('../Content/Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# ---
# Not the same as edges (mathematically)
# Useful for shape analysis, object detection, recognition

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayed', gray)

# ---

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blurred', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# ---
# Thresholding
# Can use this instead of canny method
# looks at image and tries to binarize image

# (img, min value, max value, type of thresholding)
# binary -> one or the other
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# ---
# Finding Contours
# Returns contours & hierarchies

# Pass in (img, what kind of contours you want to find, method of finding contours)
# Contours -> list of all contours found in the image
# Hierarchies -> hierarchical representation of all the contours

# RETR_LIST -> mode of how the method returns contours (retrieves certain different contours)

# CHAIN_APPROX_NONE -> Contour approximation method (how we want to approximate contours)
    # CHAIN_APPROX_SIMPLE -> approximates the points / contours and compresses it into the most sense
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# finding # of contours found
print(f'{len(contours)} contour(s) found')

# ---
# Visualizing/Drawing contours
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)