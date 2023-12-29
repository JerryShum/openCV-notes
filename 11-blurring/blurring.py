import cv2 as cv

img = cv.imread('../Content/Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# ---
# What goes on when we apply blur

# Kernel -> a window that you draw over an image (3x3 (3 kernel size) square over a specific portion of an image) -> something happens to the middle pixel as a result of the surrounding pixels
# The kernel window will slide to the right and down over the process

# ---
# Averaging
# Kernel window will compute the sensitivity of the middle pixel, as a result of the surrounding pixels

average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# ---
# Gaussian
# Does the same thing as average -> each surrounding pixel is given a weight, the average of the weights gives the value for the center
# Gets less blurring compared to average but is more "natural"

# SigmaX = standard deviation for x direction
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss Blur', gauss)

# ---
# Median Blurring
# Same as average blur but finds the median of the surrounding pixel
# More effective at reducing noise compared to gaussian and average

median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# ---
# Bilateral
# Applies blurring but retains the edges

# Diameter of 5
# Sigmacolor = 15
# Spacesigma = 15 -> indicating that you want pixels from "15" far away to influence the middle pixel value

bilateral = cv.bilateralFilter(img, 100, 15, 50)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)