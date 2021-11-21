import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')
#greyscale filter
def greyscale(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return greyscale

#making the greyscale image
a1 = greyscale(image)

filename = 'greyscale.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a1)

