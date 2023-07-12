import cv2

a = cv2.VideoCapture("resources/tut_02.mp4")

while True:
    success, img = a.read()

    if success:
        cv2.imshow("video", img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

a.release()
cv2.destroyAllWindows()
