import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')


def sharpen(img):
    kernel = np.array([[-1,-1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    img_sharpen = cv2.filter2D(img, -1, kernel)
    return img_sharpen

a1 = sharpen(image)
filename = 'sharpened_image.jpg'
cv2.imwrite(filename, a1)