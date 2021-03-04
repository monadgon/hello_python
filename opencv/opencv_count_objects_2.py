import cv2
from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt

# image = cv2.imread('opencv\pills2.jpg')
# edges = cv2.Canny(image,100,200)
# cv2.imshow('edges', edges)
# cv2.waitKey(0)

# grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('grayimg', grayimg)
# cv2.waitKey(0)

grayimg = io.imread('opencv\pills2.jpg', as_gray=True)
val = filters.threshold_otsu(grayimg)
drops = ndimage.binary_fill_holes(grayimg < val)
plt.imshow(drops, cmap='gray')
plt.show()

from skimage import measure
labels = measure.label(drops)
print(labels.max())