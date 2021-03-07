import cv2

# img_path = 'opencv\Containers.png' # OK
#img_path = "opencv\pills_simple.png" #105?
#img_path = "opencv\pills_simple_box.png"# 100, OK at Canny(_,50, 220)
img_path = "C:\PjtPython\hello_python\opencv\images\pillls_box_001.png"
#img_path = "C:\\PjtPillCounter\\images_pill\\20210125 135858-1.png" # 1920x1080 NG
image= cv2.imread(img_path)
#image = cv2.resize(image,(0,0),fx=2, fy=2) # 2확대 95
#cv2.imshow('image', image)
#cv2.waitKey(0)

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#canny= cv2.Canny(gray, 50,200)#102
#canny= cv2.Canny(gray, 50,250)#96
canny= cv2.Canny(gray, 20,220) #100 def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
cv2.imshow("canny", canny)
cv2.waitKey(0)

contours, hierarchy= cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

number_of_objects_in_image= len(contours)

print ("The number of objects in this image: ", str(number_of_objects_in_image))
