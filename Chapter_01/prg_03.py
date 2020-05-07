# Reading & showing a video
import cv2

cap = cv2.VideoCapture(0)  # webcam object
cap.set(3, 640)  # 3 is property id for width
cap.set(4, 480)  # 4 is property id for height

cap.set(10, 100)  # 10 is property id for brightness

# We need a loop to iterate through all the frames of the video
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Terminate with letter 'q'
        break
