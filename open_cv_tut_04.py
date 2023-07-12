#resizing the images
import cv2

img=cv2.imread("resources/cat.jpeg")
print(img.shape)
#(350, 528, 3)
resize=cv2.resize(img,(300,400))
resize2=cv2.resize(img,(500,600))  

cv2.imshow("im1",img)
cv2.imshow("im2",resize)
cv2.imshow("im3",resize2)


cv2.waitKey(0)