import cv2 as cv
import numpy as np

# Pixels are turned OFF with a value of 0, and ON with a value of 1

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# ---
# bitwise AND (AND'S all of the pixels) (only displays the overlapping pixels)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And', bitwise_and)

# ---
# bitwise OR (OR's all of the pixels) (overlapping and non-overlapping)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# ---
# bitwise XOR (non-overlapping regions)
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# ---
# bitwise NOT -> reverses the 1's and 0's of an image
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)
cv.waitKey(0)