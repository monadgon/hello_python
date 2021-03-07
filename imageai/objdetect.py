import cv2
import matplotlib.pyplot as plt
import cvlib as cv 
from cvlib.object_dectection import draw_bbox
im = cv2.imread("C:\PjtPython\hello_python\opencv\images\cars-001.png")
bbbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print("number of cars in image: ", str(label.count('car')))
