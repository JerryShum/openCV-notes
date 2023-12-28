import cv2 as cv
import numpy as np

# split and merge colour channels
# image channels - rgb
# split an image into respective color channels BGR --> Blue, green, and red components

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge back together

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue1', blue)
cv.imshow('Green1', green)
cv.imshow('Red1', red)


cv.waitKey(0)