import cv2
import numpy as np
img = cv2.VideoCapture("resources/video.mp4")

min_width_rec=80
min_height_rec=80
algo = cv2.bgsegm.createBackgroundSubtractorMOG()
line_position=550

def center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return(cx,cy)

car_list=[]
offset=6
counter=0

while True:
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    # apply on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernal)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernal)

    cont,h= cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame,(25,line_position),(1200,line_position),(255,127,0),3)

    for (i,c) in enumerate(cont):
        (x,y,w,h)=cv2.boundingRect(c)
        val_counter=(w>=min_width_rec) and (h>=min_height_rec)
        if not val_counter:
            continue
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,500),2)

        d=center(x,y,w,h)
        car_list.append(d)

        cv2.circle(frame,d,4,(0,0,900),-1)


        for (x,y) in car_list:
            if y<(line_position + offset) and y>(line_position - offset):
                counter+=1
            cv2.line(frame,(25,line_position),(1200,line_position),(255,127,0),3)
            car_list.remove((x,y))
            #print("Car Counter : "+str(counter))


    cv2.putText(frame,"car counter : "+str(counter),(450,70),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,500),3)


    cv2.imshow("output", frame)

    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
img.release()
