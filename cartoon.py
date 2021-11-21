import cv2
import numpy as np

img = cv2.imread("download.jpeg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#find edges of image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartoonify the image
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

filename = 'cartoon.jpg'
cv2.imshow("cartoon", cartoon)
cv2.imwrite(filename, cartoon)