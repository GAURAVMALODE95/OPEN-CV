import cv2
import numpy as np

img = cv2.imread("roads.jpg")
# resizing the image
desired_width = 800
aspect_ratio = img.shape[1] / img.shape[0]
desired_height = int(desired_width / aspect_ratio)
new_img = cv2.resize(img, (desired_width, desired_height))

grey=cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)#converted to gray
blurred = cv2.GaussianBlur(grey, (3,3), 0)
#thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

edges=cv2.Canny(new_img,500,700)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(new_img, contours, -1, (0,0,255), 2)

cv2.imshow("output", new_img)
cv2.waitKey(0)
