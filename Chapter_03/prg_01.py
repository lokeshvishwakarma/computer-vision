# Resizing and cropping
# In OpenCV convention origin is at the top-left of the image
# Horizontal is the X-axis(+ve toward right) and vertical is Y-axis(+ve downwards)
import cv2
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

image_path = curr_dir + '/../resources/fashion_lo.jpg'
img = cv2.imread(image_path)
print('Original Image', img.shape)
cv2.imshow('Original Image', img)
cv2.waitKey(5000)

resized_img = cv2.resize(img, (360, 224))  # (width, height)
print('Resized Image', resized_img.shape)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(5000)

cropped_img = img[0:360, 0:499]  # Slice of height, width
print('Cropped Image', cropped_img.shape)
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(5000)
