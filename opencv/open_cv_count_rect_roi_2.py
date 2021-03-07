# 2021.03.08
# ROI를 추출

import cv2
import numpy as np

def ROITest():
    imgFile = "C:\\PjtPillCounter\\images_pill\\20210125 135858-1.png"
    img = cv2.imread(imgFile)

    print(img.shape) # (1080, 1920, 3) rows, cols, channels

    # ROI (Region of interest)
    cv2.rectangle(img, (422, 253), (1350, 1000), (0, 255, 0), 3)
    cv2.imshow('img', img)


    # Cut image
    subimg = img [253:1000 , 422:1350]
    cv2.imshow('cutting',subimg)

    # 원본이미지상의 좌표상 (50,400) , (150,550) 범위에 커트한 이미지 삽입
    #img[400:550 , 50:150] = subimg

    # 합쳐진 이미지
    #cv2.imshow('after',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

ROITest()

#[출처] Python OpenCV 시작 (8) - 이미지 ROI 설정|작성자 박원영

# https://www.youtube.com/results?search_query=opencv+count+object
# Next https://www.youtube.com/watch?v=rRcwuQGDFOA&t=560s