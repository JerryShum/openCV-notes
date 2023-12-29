import cv2 as cv


img = cv.imread('../Content/Resources/Photos/park.jpg');
cv.imshow('Park', img)

# ---
# How to switch between color spaces (RGB, BGR, GRAYSCALE)

# RGB and BGR are opposites -> some other libraries will use RGB (inverse colors) while openCV uses BGR

# You cannot convert some formats to another format directly (HSV to Grayscale) -> Must convert to BGR first and then Grayscale

# BGR -> Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY);
cv.imshow("Grayed", gray)

# BGR -> HSV (Hue Saturation Value) (based on how humans perceive color)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*A*B)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)


cv.waitKey(0)