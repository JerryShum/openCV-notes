import cv2 as cv
import numpy as np

img = cv.imread('../Content/Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translations
def translate(img, x, y):
    # Translation matrix
    transMat = np.float32([[1,0,x],[0,1,y]])
    # Width and Height
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

# -x -> left
# -y -> up
# x -> right
# y -> down

# Right 100, down 100
translated = translate(img, 100, 100)
cv.imshow("translated", translated)

# ---
# Rotation

def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) 
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

# Rotating an image 45 degrees
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# You can rotate a rotated img
rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated_rotated', rotated_rotated)

# ---
# Resizing Image

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# ---
# Flipping

# Flip: 0 -> over x-axis
# 1-> over y-axis
# -1 -> over both
flip = cv.flip(img, -1)
cv.imshow('Flipped', flip)

# ---
# Cropping

cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)