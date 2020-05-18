# Face Detection (Viola & Jones Method)
# Requires cascades(xml files which are trained models)
# We'll be using default cascades provided by openCV
import os
import cv2

curr_dir = os.path.dirname(os.path.abspath(__file__))
image_path = curr_dir + '/../resources/lena.png'
cascade_path = curr_dir + '/../resources/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(cascade_path)
img = cv2.imread(image_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Result', img)

cv2.waitKey(0)
