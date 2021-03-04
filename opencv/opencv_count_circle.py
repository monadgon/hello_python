#!/usr/bin/python3.7.3
#OpenCV 4.2, Raspberry pi 3/3b/34b, Buster ver
#Date: 2nd February, 2020

import numpy as np
import cv2
import sys

def main():
    fn = 'C:\\PjtPython\\hello_python\\opencv\\bottles.png'
    src = cv2.imread(fn)
    if src is None:
        print("fail to load image: " + fn)
        sys.exit()

    img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    cimg = src.copy() # numpy function

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 69, 21, 9, 26)
    counter = 0
    if circles is not None: # Check if circles have been found and only then iterate over these and add them to the image
        _a, b, _c = circles.shape
        for i in range(b):
            # TypeError: Argument 'radius' is required to be an integer 
            cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), int(circles[0][i][2]), (0, 0, 255), 2, cv2.LINE_AA)
            cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA)  # draw center of circle
            counter += 1

        print(f'counter ;', counter)
        cv2.imshow("detected circles", cimg)

    cv2.imshow("source", src)
    cv2.waitKey(0)
    print('Done')


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()