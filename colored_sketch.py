import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')

def color_sketch(img):
    sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_color

    
a1 = color_sketch(image)
filename = 'color_sketch.jpg'
cv2.imwrite(filename, a1)
