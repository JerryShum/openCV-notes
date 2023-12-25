import cv2 as cv
import numpy as np

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)


# creating a blank image (width, height, and number of colour channels)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint image with a colour
for x in range(0, 100):
    for y in range(100, 200):
        blank[y, x] = (0, 255, 0)

cv.imshow('Green', blank)

def draw_rectangle(frame, point1, point2, colour):
    cv.rectangle(frame, point1, point2, colour, thickness=1)
    # -1 == cv.FILLED
    # 0 same thing as 1 thickness bruh
    
draw_rectangle(blank, (0, 0), (250, 250), (0, 255, 0))
cv.imshow('New Rectangle', blank)

# frame, midpoint, radius, colour, thickness
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# frame, from_point, to_point, colour, thickness
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

cv.putText(blank, 'Nehmat Farooq, Certified Clutch Performer', (0, 100), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 255))
cv.imshow('Nehmat', blank)

cv.waitKey(0)