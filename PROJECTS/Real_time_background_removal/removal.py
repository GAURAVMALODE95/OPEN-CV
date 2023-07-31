import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap=cv2.VideoCapture("video.mp4")
imgbg=cv2.imread("images/img_4.jpg")
segmentor=SelfiSegmentation()
fps=cvzone.FPS()

while True:
    sucess,img=cap.read()
    imgbg_resized = cv2.resize(imgbg, (img.shape[1], img.shape[0]))

    out = segmentor.removeBG(img, imgbg_resized, threshold=0.75)
    #out = cv2.resize(out, (720, 1280))

    cv2.imshow("out1",img)
    cv2.imshow("out",out)

    cv2.waitKey(1)
