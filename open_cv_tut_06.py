#wrap prespective of image
import cv2
import numpy as np
width,height=528,350
img=cv2.imread("resources/cat.jpeg")
pts=np.float32([[176,7],[367,9],[188,209],[339,235]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
mat=cv2.getPerspectiveTransform(pts,pts2,2)
imgout=cv2.warpPerspective(img,mat,(width,height))

cv2.imshow("im1",img)
cv2.imshow("im2",imgout)
cv2.waitKey(0)