import cv2 as cv

capture = cv.VideoCapture('Videos/kitten.mp4') # can take in integer arguments liek 0, 1, 2, 3 (if camera, most of the time 0), or a path to a video file

# while loop and read video frame by frame

while True:
    isTrue, frame = capture.read() # reads the video frame, isTrue whether the frame was successfuly read or not
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()


# -215 aassertion error : two cases 1. video ran out of rames 2. path does not exist. aka a frame could not be found