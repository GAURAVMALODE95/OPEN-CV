import cv2

# Load video file instead of capturing from the webcam
cap = cv2.VideoCapture("traffic.mp4")

cap.set(3, 1280)
cap.set(4, 720)

classnames = []
classfile = 'coco.names'
with open(classfile, 'rt') as f:
    classnames = f.read().rstrip('\n').split('\n')

config_path = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightspath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightspath, config_path)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    
    # Check if the video has reached its end
    if not success:
        break
    
    classIds, confs, bbox = net.detect(img, confThreshold=0.6)
    print(classIds, bbox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 0, 255), thickness=4)
            cv2.putText(img, classnames[classId-1], (box[0]+10, box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (123, 2, 124), 2)

    cv2.imshow("output", img)
    key = cv2.waitKey(1)

    # Press 'q' to quit the loop
    if key == ord('q'):
        break

# After the loop
cap.release()
cv2.destroyAllWindows()
