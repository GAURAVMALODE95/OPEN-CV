#basic functions
import cv2
import numpy as np
kernal=np.ones((5,5),np.uint8)
img=cv2.imread("resources/cat.jpeg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(img,(7,7),0)
imgcanny=cv2.Canny(img,200,180)#edge detection
imgdilation=cv2.dilate(imgcanny,kernal,iterations=1)#dilation
imgerode=cv2.erode(imgdilation,kernal,iterations=1)
cv2.imshow("Output1",imgGray)
cv2.imshow("Output2",imgBlur)
cv2.imshow("Output3",imgcanny)
cv2.imshow("Output4",imgdilation)
cv2.imshow("Output5",imgerode)

cv2.waitKey(0)