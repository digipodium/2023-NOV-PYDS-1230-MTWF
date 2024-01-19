import cv2, os
file = r'computervision/sample_vid2.mp4'  # <= 1
if not os.path.exists(file):
    print('video file not found')
camera = cv2.VideoCapture(file) # <= 2
while True: # <= 3
    state, frame = camera.read() # frame -> image captured, state -> boolean
    if not state:
        print("Could not access video")
        break # if state is false, stop the loop
    cv2.imshow('camera window', frame)
    if cv2.waitKey(20) == ord('q'): # <= 4
        break
camera.release()
cv2.destroyAllWindows()
