import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')

#increase significance to details in an image
def hdr_image(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr

a1 = hdr_image(image)
filename = 'hdr_image.jpg'
cv2.imwrite(filename, a1)