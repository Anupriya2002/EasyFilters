import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')

def neg_image(img):
    #invert the pixel values (subtract pixel values from 255)
    negative_img = cv2.bitwise_not(img)
    return negative_img

a1 = neg_image(image)

filename = 'neg_image.jpg'
cv2.imwrite(filename, a1)