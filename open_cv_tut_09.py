#face detection
#method by viola and jones
#positives----faces#########negatives------other than faces.
import cv2
faceCascade=cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img=cv2.imread("resources/modiji.jpg")

imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=faceCascade.detectMultiScale(imggray,1.1,4)
#to draw boxes around detected faces
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,2300),2)


cv2.imshow("output_1",img)
cv2.waitKey(0)