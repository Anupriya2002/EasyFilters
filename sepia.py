import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')

def sepia(img):
    img_sepia = np.array(img, dtype=np.float64)
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]))
    img_sepia[np.where(img_sepia > 255)] = 255 #normalize the range to ensure value does not exceed 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return img_sepia

a1 = sepia(image)
filename = 'sepia.jpg'

cv2.imwrite(filename, a1)