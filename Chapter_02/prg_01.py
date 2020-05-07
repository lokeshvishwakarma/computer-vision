# Basic grayscale, blur, edge detection, dilation, erosion functions
# erosion is opposite of dilation
import cv2
import os
import numpy as np

curr_dir = os.path.dirname(os.path.abspath(__file__))
kernel = np.ones((5, 5), np.uint8)

image_path = curr_dir + '/../resources/fashion_lo.jpg'
img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(img_gray, (15, 15), 0)
canny_image = cv2.Canny(img, 150, 150)
img_dialation = cv2.dilate(canny_image, kernel, iterations=1)
img_eroded = cv2.erode(img_dialation, kernel, iterations=1)

cv2.imshow('Gray Image', img_gray)
cv2.waitKey(2000)
cv2.imshow('Blur Image', blur_image)
cv2.waitKey(2000)
cv2.imshow('Canny Edge Image', canny_image)
cv2.waitKey(2000)
cv2.imshow('Dilated Image', img_dialation)
cv2.waitKey(2000)
cv2.imshow('Eroded Image', img_eroded)
cv2.waitKey(2000)
