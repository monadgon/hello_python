# pip install opnecv-python
# ERROR: Could not find a version that satisfies the requirement opnecv-python
# solution)
# python -m pip install opencv-python
# Successfully installed numpy-1.20.1 opencv-python-4.5.1.48
# cv2에 물결 에러를 표시할 경우, settings.json에 추가    "python.linting.pylintArgs": ["--generated-members=cv2.*"]

import cv2
#print(cv2.__version__) #4.5.1

img1 = cv2.imread("C:\\PjtPython\\hello_python\\opencv\\universe.jfif")
#print(type(img1)) # <class 'NoneType'>
#print(img1.shape) # AttributeError: 'NoneType' object has no attribute 'shape'
#print(img1.dtype)
cv2.imshow('image1', img1)


#img = cv2.imread('C:\\PjtPython\\hello_python\\opencv\\stars.bmp')
#cv2.imshow('image', img)
cv2.waitKey(0)
#cv2.destroyAllWindows()
