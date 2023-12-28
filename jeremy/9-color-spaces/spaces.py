

# switch between colour spaces
# RGB Is a colour space
# greysacle is a colour space
# HSV, LAV, 


import cv2 as cv

# shows BGR images
img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# matplotlib doesn't know it is a BGR image and displays it as an RGB image, therefore shows an inversion of colour
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

# BGR TO GREYSCALE, shows intensities in your image
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grey)

# BGR TO HSV (hue saturation value) how humans conceive colour
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*A*B)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb) # open cv.imshow by default displays in BGR, therefore we pass in an RGB image, we will get the inversion.

# can do HSV --> BGR and BGR --> HSV
# can do LAB --> BGR and BGR --> LAB
# can do greyscale to BGR

cv.waitKey(0)