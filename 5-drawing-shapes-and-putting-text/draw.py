import cv2 as cv
import numpy as np

# Making a blank image and showing it
# (500,500,3) Width, heigh, color channels
# datatype? -> uint8

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# ---
# img = cv.imread('../Content/Resources/cat.jpg')
# cv.imshow('Cat', img)

# ---
# 1. Paint image a certain colour

# [200:300, 300:400]
#  Y-axis -> paint pixels from 200 - 300 Green
#  X-axis -> paint pixels from 300 - 400 Green
# blank[125:375, 125:375] = 0,255,0
# cv.imshow('Red', blank)

# ---
# 2. Draw Rectangle with border
# (what to draw on, point1, point2, colour, thickness)
# Thickness = -1 -> filled rectangle -> 1 = 0 -> thin border
# blank.shape[1] = x (width), blank.shape[2] = y (height)

# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness= cv.FILLED)
# cv.imshow("Rectangle", blank)


# ---
# 3. Draw Circle
# (what to draw on, (mid point), radius, colour, thickness)

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 200, (0,0,255), -1)
# cv.imshow("Circle", blank)

# ---
# 4. Draw Line

cv.line(blank, (0,0), (500,500) , (255,255,255), 3, 2)
cv.imshow("line", blank)

# ---
# 5. Write Text
cv.putText(blank, 'Hello, my name is Jerry', (0, 225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)

