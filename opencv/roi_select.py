# 관심영역 표시 (roi.py)
# https://bkshin.tistory.com/entry/OpenCV-6-dd

import cv2
import numpy as np

img_path = 'opencv\images\img.jpg'
img = cv2.imread(img_path)      # 이미지를 numpy 배열로 

x=320; y=150; w=50; h=50        # roi 좌표
roi = img[y:y+h, x:x+w]         # roi 지정        ---①

print(roi.shape)                # roi shape, (50,50,3)

img2 = roi.copy()

img[y:y+h, x+w:x+w+w] = roi # 새로운 좌표에 roi 추가, 태양 2개 만들기
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0)) # 2개의 태양 영역에 사각형 표시

cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0)) # roi 전체에 사각형 그리기 ---②

cv2.imshow("img", img)
cv2.imshow("roi", img2)     # roi 만 따로 출력

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()
