import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Kernel blurring (Averaging Method)
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur (7,7)', average)

# Gaussian Blurring
# instead of computing surrounding pixel intensity, each pixel is given a weight and the average of the product of those weights, then it gives you value of true center
std_deviation = 0
gauss = cv.GaussianBlur(img, (7, 7), sigmaX=std_deviation)
cv.imshow('Gauss', gauss)

# Median Blur (same thing as averaging, but finds median of surrounding pixels, more effective in reducing noise as opposed to averaging and gaussian blur)
# for advanced computing vision project with lots of noise maybe
median = cv.medianBlur(img, 7) # assumes kernel size is a square
cv.imshow('Median Blur', median)

# Bilateral blurring
# most effective, for advanced computer vision project because of "how" it blurs
# applies blurring but retains edges
bilateral = cv.bilateralFilter(img, 15, sigmaColor=100, sigmaSpace=15) # d = diameter of pixel neighbourhood, sigmaColor = larger value => more colours in neighbourhood that will be considered, sigmaSpace = larger values => pixels further out from center will influence blurring calculation
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)