import cv2 as cv
import numpy as np

img = cv.imread('../Content/Resources/Photos/park.jpg')
cv.imshow('Park', img)


# ---
# Splitting into different color channels

# Shown as a grayscale image (lighter regions = higher concentration of that color, darker regions = almost no concentration of the color)
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green',g)
cv.imshow('Red',r)


# (427,620,3)
# 3 = 3 color channels (3 diff colors)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# ---
# Merging
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

# ---
# Displaying color channels with actual color

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)