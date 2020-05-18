# Contour & Shape Detection
import os
import cv2
import numpy as np

curr_dir = os.path.dirname(os.path.abspath(__file__))
image_path = curr_dir + '/../resources/shapes.png'


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


img = cv2.imread(image_path)


def get_contours(img):
    # image, retrieval method(retrieve extreme outer corners), approximation method
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print('area', area)
        if area >= 500:
            cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            print('perimeter', perimeter)
            # contour, resolution(epsilon)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            print('approx', len(approx))
            obj_corner = len(approx)
            # draw bounding box taround the object
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 150), 2)
            if obj_corner == 3:
                object_type = 'Triangle'
            elif obj_corner == 4:
                aspect_ratio = w / float(h)
                if 0.95 < aspect_ratio < 1.05:
                    object_type = 'Square'
                else:
                    object_type = 'Rectangle'
            elif obj_corner > 4:
                object_type = 'Circle'
            else:
                object_type = 'None'
            cv2.putText(img_contour, object_type, (x + (w // 2) - 10, y + (h // 2) - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0,), 2)


img_contour = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blur, 30, 30)
get_contours(img_canny)

img_blank = np.zeros_like(img)
# cv2.imshow('Original', img)
# cv2.imshow('Gray', img_gray)
# cv2.imshow('Blur', img_blur)

img_stack = stackImages(0.5, ([img, img_gray, img_blur],
                              [img_canny, img_contour, img_blank]))
cv2.imshow('Stack', img_stack)

cv2.waitKey(0)
