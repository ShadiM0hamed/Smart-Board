# -*- coding: utf-8 -*-
"""
@author: %Shady 🎶
Faculty of Artificial Intelligence
shadimhamed6@gmail.com

"""

import cv2
import time
import mediapipe as mp
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

pv = (0,0)

counterr = 1

mpDraw = mp.solutions.drawing_utils
ptime = 0
counter = []
fincon = []
ftips = [8, 12, 16, 20]
l = []
mphand = mp.solutions.hands
hands = mphand.Hands(False,6,1,0.3,0.3)

white = cv2.imread("C:\\Users\\shady\\OneDrive\\Pictures\\Screenshots\\white.png")

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    h , w , c = frame.shape
    ctime = time.time()
    fps = 1 /(ctime-ptime)
    ptime = ctime
    
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultsh = hands.process(imgRGB)
    
    if resultsh.multi_hand_landmarks:
            
            for hand in (resultsh.multi_hand_landmarks):
                y = []
                mpDraw.draw_landmarks(frame,hand, mphand.HAND_CONNECTIONS)
                S=0
                for  i in hand.landmark:
                    
                    y.append([S,i.x,i.y,i.z])
                    cv2.circle(frame, (int(i.x*w),int(i.y*h)), 1,(100,50,200),2)
                    S=S+1
                    fincon = []
                if y[4][1]> y[5][1]:
                    fincon.append(1)
                else:
                    fincon.append(0)
                for fing in ftips:
                    

                    if y[fing][2]< y[fing-2][2]:
                        fincon.append(1)
                    else:
                        fincon.append(0)

                print(fincon)

                cv2.circle(frame, (int(y[8][1]*w),int(y[8][2]*h)), 3,(150,50,70),2)
                cv2.circle(frame, (int(y[12][1]*w),int(y[12][2]*h)), 3,(150,50,70),2)
            
    l = []
    if [0,1,0,0,0] == fincon or [1,1,0,0,0] == fincon:
        if counterr>1:
            cv2.circle(white, (int(y[8][1]*w*2.1343),int(y[8][2]*h*1.6)), 7,(150,50,70),-1)
            cv2.line(white,(pv),(int(y[8][1]*w*2.1343),int(y[8][2]*h*1.6)),(150,50,70),7)
            cv2.putText(white, "Typing", (50, 60),cv2.FONT_HERSHEY_COMPLEX, 0.5 , (170,160,110), 2)
        pv = (int(y[8][1]*w*2.1343),int(y[8][2]*h*1.6))
        counterr = counterr +1 
    elif ((fincon == [1,1,1,1,1]) or (fincon == [0,1,1,1,1])):
        counterr = 1
    elif fincon == [0,0,0,0,0] or fincon == [1,0,0,0,0]:
        white = cv2.imread("C:\\Users\\shady\\OneDrive\\Pictures\\Screenshots\\white.png")
        cv2.putText(white, "Clear", (50, 60),cv2.FONT_HERSHEY_COMPLEX, 0.5 , (255,0,0), 2)

    cv2.imshow("white", white)
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if c == 27 :
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()
cap.release()