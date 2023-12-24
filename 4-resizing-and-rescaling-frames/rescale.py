import cv2 as cv

def rescaleFrame(frame, scale = 0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# ---

def changeRes(width,height):
    # ONLY WORKS ON LIVE VIDEO
    capture.set(3,width)
    capture.set(4,height)

# ---

img = cv.imread("../Content/Resources/Photos/cat_large.jpg")
cv.imshow("Cat", img)

# ---

capture = cv.VideoCapture(0)

# Loop to read video (Reads frame by frame)
while True:
    # returns frames, 
    isTrue, frame = capture.read()
    
    frame_resized=rescaleFrame(frame)
    
    cv.imshow('Video', frame_resized)
    
    # if d is pressed, break
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
    # read frame -> wait 20 ms, 

cv.waitKey(0)

# ---

resized_image = rescaleFrame(img, frame_resized)
cv.imshow("Resized Image", resized_image)

