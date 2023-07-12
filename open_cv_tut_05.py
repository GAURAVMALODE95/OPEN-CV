#shapes and texts on image
import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]=0,0,999....red color

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),10)
#rectrangle
cv2.rectangle(img,(0,0),(100,100),(0,0,244),10)
cv2.circle(img,(300,30),20,(120,0,0),10)



#text on images

cv2.putText(img,"hello",(10,200),cv2.FONT_HERSHEY_COMPLEX,3,(150,0,0),3)
cv2.imshow("img",img)
cv2.waitKey(0)



