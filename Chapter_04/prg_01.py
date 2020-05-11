# Shapes and Texts
import cv2
import numpy as np

# Create a matrix with zeroes
img = np.zeros((512, 512, 3), np.uint8)  # This creates a black image of 512 x 512
print('Original Image', img.shape)
# img[:] = 255, 0, 0  # Puts blue color to the full image
img[200:300, 100:300] = 255, 0, 0  # Puts blue color to the specified range of image
# Because in OpenCV are BGR instead of RGB


# cv2.line(img, (0, 0), (200, 300), (0, 255, 255))  # takes img, start point, end point, color
cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 255))  # here end point is given as the corners of the img
cv2.rectangle(img, (20, 20), (250, 300), (0, 0, 255), 5)  # creates outlined rectangle
# cv2.rectangle(img, (20, 20), (250, 300), (0, 0, 255), cv2.FILLED)  # creates filled rectangle
cv2.circle(img, (400, 400), 60, (0, 255, 255), 3)
cv2.putText(img, 'OpenCV', (300, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 230), 1)
cv2.imshow('Original Image', img)
cv2.waitKey(3000)
