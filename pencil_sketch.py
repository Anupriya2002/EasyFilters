import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')

def pencil_sketch(img):
    sk_gray = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_gray

a1 = pencil_sketch(image)
filename = 'pencil_sketch.jpg'
cv2.imwrite(filename, a1)