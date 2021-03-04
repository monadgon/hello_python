import cv2

# img_path = 'opencv\Containers.png' # OK
img_path = "opencv\pills_simple.png" #105?
#img_path = "opencv\pills_simple_box.png"# 102
image= cv2.imread(img_path)
#image = cv2.resize(image,(0,0),fx=2, fy=2) # 2확대 95
#cv2.imshow('image', image)
#cv2.waitKey(0)

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#canny= cv2.Canny(gray, 50,200)#102
#canny= cv2.Canny(gray, 50,250)#96
canny= cv2.Canny(gray, 50,220)#100
cv2.imshow("canny", canny)
cv2.waitKey(0)

contours, hierarchy= cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

number_of_objects_in_image= len(contours)

print ("The number of objects in this image: ", str(number_of_objects_in_image))
