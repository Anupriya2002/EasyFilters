import cv2
import numpy as np
import scipy

image = cv2.imread('download.jpeg')

from scipy.interpolate import UnivariateSpline
def LookupTable(x,y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))


def cooler(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel  = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    cool = cv2.merge((blue_channel, green_channel, red_channel ))
    return cool

a1 = cooler(image)
filename = 'cooler_image.jpg'

cv2.imwrite(filename, a1)