import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')

def bright(img, beta_value):
    img_bright = cv2.convertScaleAbs(img, beta=beta_value)
    return img_bright

#a brightened image
a1 = bright(image, 60)
filename = 'brightened-image.jpg'
#save the image
cv2.imwrite(filename, a1)

#a darker image
#can darken an image using a negative beta value
a3 = bright(image, -60)
filename = 'darkened_image.jpg'
cv2.imwrite(filename, a3)