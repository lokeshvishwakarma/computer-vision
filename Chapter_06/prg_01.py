# Joining Images
import os
import cv2
import numpy as np

curr_dir = os.path.dirname(os.path.abspath(__file__))
image_path = curr_dir + '/../resources/fashion_lo.jpg'
img = cv2.imread(image_path)


# Stacking requires all the images with same number of channels, as we are dealing with matrices
# horizontal_stack = np.hstack((img, img))
# print(horizontal_stack, type(horizontal_stack))
# vertical_stack = np.vstack((img, img))

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# cv2.imshow('Horizontal Stack', horizontal_stack)
# cv2.waitKey(3000)
# cv2.imshow('Vertical Stack', vertical_stack)
# cv2.waitKey(3000)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_stack = stackImages(0.5, ([img, img_gray, img], [img, img, img]))
cv2.imshow('Stack', img_stack)
cv2.waitKey(3000)
