# https://medium.com/analytics-vidhya/detecting-and-counting-objects-with-opencv-b0f59bc1e111

import sys
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

img_path = "opencv\pills2.jpg"
image = cv2.imread(img_path)
if image is None:
    print('ERROR to read an image') 
    sys.exit()
#cv2.namedWindow("src", flags=cv2.WINDOW_KEEPRATIO)
cv2.imshow("src", image)
cv2.waitKey(0)

#If you notice, you can see the bright spots on the coin. And again, there are sharp lines on the money. 
# This will reduce efficiency when filtering this image. So let’s make our picture available.
#image_blur = cv2.medianBlur(image, 25)
#cv2.namedWindow("medianBlur", flags=cv2.WINDOW_KEEPRATIO)
#cv2.imshow("medianBlur", image_blur)
#cv2.waitKey(0)

# One of the most important steps in object detection is to make the picture colorless. 
# So we will turn our picture into a black and white tone. This is generally used in all object detection methods.
# This allows the image to run more efficiently because it reduces the number of scans.
image_blur_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.namedWindow("COLOR_BGR2GRAY", flags=cv2.WINDOW_KEEPRATIO)
cv2.imshow("COLOR_BGR2GRAY", image_blur_gray)
cv2.waitKey(0)

# If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value 
# (may be black). The function used is cv2.threshold. First argument is the source image, which should be a grayscale image. 
# Second argument is the threshold value which is used to classify the pixel values. Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.
# 
# I preferred the “THRESH_BINARY_INV” method because I want the coins to remain white here and the rest to be black. 
# You can choose the appropriate values ​​according to your own picture.
image_res ,image_thresh = cv2.threshold(image_blur_gray,240,255,cv2.THRESH_BINARY_INV)

# Now we will create a kernel here. This kernel will be 3x3 size.
kernel = np.ones((3,3),np.uint8)

# Then we will apply this to our picture as follows.
opening = cv2.morphologyEx(image_thresh,cv2.MORPH_OPEN,kernel)

# Now it is time to replace the value of each pixel with the distance to the nearest background pixel using distanceTransform. 
# We will do this using the distanceTransform method. When we apply this method, our array type turns into float32. So we will 
# do 2 more steps and convert our array back to uint8 type.
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, last_image =  cv2.threshold(dist_transform, 0.3*dist_transform.max(),255,0)
last_image = np.uint8(last_image)
cv2.namedWindow("threshold", flags=cv2.WINDOW_KEEPRATIO)
cv2.imshow("threshold", last_image)
cv2.waitKey(0)

# We have the last 2 blocks of code left. In this section, we will now process the counting of objects and recording the positions of the objects. We use findContours to detect objects. Then we make our array regular with the grap_contours method.
cnts = cv2.findContours(last_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("count:", len(cnts))

def display(img,count,cmap="gray"):
    cv2.namedWindow("Final", flags=cv2.WINDOW_KEEPRATIO)
    cv2.imshow("Final", img)
    cv2.waitKey(0)

    f_image = cv2.imread(img_path)
    fig, axs = plt.subplots(1,2,figsize=(12,5))
    fig.suptitle('Horizontally stacked subplots')
    axs[0].imshow(f_image,cmap="gray")
    axs[1].imshow(img,cmap="gray")
    axs[1].set_title("Total Money Count = {}".format(count))
    #fig, (ax1, ax2) = plt.subplots(1,2)
    #fig.suptitle('Horizontally stacked subplots')
    #ax1.imshow(f_image)
    #ax2.imshow(img)
    plt.show()

for (i, c) in enumerate(cnts):
    ((x, y), _) = cv2.minEnclosingCircle(c)
    cv2.putText(image, "#{}".format(i + 1), (int(x) - 45, int(y)+20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

display(image,len(cnts))