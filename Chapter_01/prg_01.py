# Reading & showing an image
import cv2
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
print('Package imported:', cv2.__version__)
print('Current Directory:', curr_dir)

image_path = curr_dir + '/../resources/fashion_lo.jpg'
img = cv2.imread(image_path)
print(img)
cv2.imshow('Output', img)
cv2.waitKey(5000)
