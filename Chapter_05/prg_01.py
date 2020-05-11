# Warp Perspective
import os
import cv2
import numpy as np

curr_dir = os.path.dirname(os.path.abspath(__file__))
image_path = curr_dir + '/../resources/cards_01.jpg'
img = cv2.imread(image_path)

# height, width = img.shape[0], img.shape[1]
width, height = 250, 350
print(width, height)
pts1 = np.float32([[875, 275], [1124, 241], [1197, 580], [910, 604]])  # coordinates are of corners of the card
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # coordinates are of corners of the card

matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_output = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow('Original Image', img)
cv2.waitKey(3000)
cv2.imshow('Original Image', img_output)
cv2.waitKey(3000)
