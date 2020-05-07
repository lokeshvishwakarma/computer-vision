# Reading & showing a video
import cv2
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

video_path = curr_dir + '/../resources/Sunrise.mp4'
cap = cv2.VideoCapture(video_path)

# We need a loop to iterate through all the frames of the video
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Terminate with letter 'q'
        break
