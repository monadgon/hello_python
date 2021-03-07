import sys
import cv2
import numpy as np

img_path = "C:\\PjtPillCounter\\images_pill\\20210125 135858-1.png" # 1920x1080
image= cv2.imread(img_path)
#image = cv2.resize(image,(0,0),fx=2, fy=2) # 2확대 95
#cv2.imshow('image', image)
#cv2.waitKey(0)

x=422; y=253; w=400; h=200        # roi 좌표
roi = image[y:y+h, x:x+w]         # roi 지정, 관심영역 시작 좌표가 (x,y)이고, 폭이 w 높이가 h일 때, y행에서 y+h행까지, x열에서 x+w열까지

print(roi.shape)                  # roi shape, (827, 912, 3)

img2 = roi.copy()

cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0), 5) # roi 전체에 사각형 그리기 ---②
cv2.imshow("image", image)
cv2.waitKey(0)
sys.exit()

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


canny= cv2.Canny(gray, 50,220) #100 def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
cv2.imshow("canny", canny)
cv2.waitKey(0)

contours, hierarchy= cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

number_of_objects_in_image= len(contours)

print ("The number of objects in this image: ", str(number_of_objects_in_image))
