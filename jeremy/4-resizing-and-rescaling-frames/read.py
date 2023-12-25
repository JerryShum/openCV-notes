import cv2 as cv

# we rescale to process quicker

def rescale_frame(frame, scale=0.25):
    new_width = int(frame.shape[1] * scale)
    new_height = int(frame.shape[0] * scale)
    dimensions = (new_width, new_height)
    new_image = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    return new_image

capture = cv.VideoCapture('Videos/dog.mp4')

# good for live videos
def change_resolution(width, height):
    capture.set(3, width) # 3 references width in class
    capture.set(4, height) # 4 references height in
    
    

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame)
    cv.imshow('Video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.reease()
cv.destroyAllWindows()