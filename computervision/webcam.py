import cv2
# webcam 1 -> 0 idx
# webcam 2 -> 1 idx
camera = cv2.VideoCapture(0)
while camera.isOpened():
    state, frame = camera.read() # frame -> image captured, state -> boolean
    if not state:
        print("Could not access camera")
        break # if state is false, stop the loop
    cv2.imshow('camera window', frame)
    if cv2.waitKey(1) == ord('q'): # if q is pressed stop the loop
        break
camera.release()
cv2.destroyAllWindows()
