#color detection in an image
import cv2
def empty(a):
    pass


cv2.namedWindow("t1")
cv2.resizeWindow("t1",640,240)
cv2.createTrackbar("Hue min","t1",0,179,empty)
cv2.createTrackbar("Hue max","t1",179,179,empty)
cv2.createTrackbar("sat min","t1",0,179,empty)
cv2.createTrackbar("sat max","t1",255,179,empty)
cv2.createTrackbar("val min","t1",0,255,empty)
cv2.createTrackbar("val min","t1",255,255,empty)



while True:
    img=cv2.imread("resources/orange.jpg")
    hmin=cv2.getTrackbarPos("Hue min","t1",)
    hmax=cv2.getTrackbarPos("Hue max","t1",)
    smin=cv2.getTrackbarPos("sat min","t1",)
    smax=cv2.getTrackbarPos("sat max","t1",)
    vmin=cv2.getTrackbarPos("val min","t1",)
    vmax=cv2.getTrackbarPos("val min","t1",)
    img=cv2.imread("resources/orange.jpg")
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("i0",img)
    cv2.imshow("i1",imghsv)
    cv2.waitKey(1)