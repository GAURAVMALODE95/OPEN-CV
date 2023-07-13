#joining images toghter
import cv2
import numpy as np

img=cv2.imread("resources/cat.jpeg")

hr=np.hstack((img,img))
vr=np.vstack((img,img))
cv2.imshow("1",hr)
cv2.imshow("2",vr)

cv2.waitKey(0)