import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
while True:
    seccess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h , w , c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 8:
                    cv2.circle(img, (cx, cy), 13, (255, 0, 255), cv2.FILLED)
                if id == 4:
                    cv2.circle(img, (cx, cy), 13, (255, 0, 255), cv2.FILLED)
                if id == 12:
                    cv2.circle(img, (cx, cy), 13, (255, 0, 255), cv2.FILLED)
                if id == 16:
                    cv2.circle(img, (cx, cy), 13, (255, 0, 255), cv2.FILLED)
                if id == 20:
                    cv2.circle(img, (cx, cy), 13, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, 'fps :' +str(int(fps)), (10, 60), cv2.FONT_HERSHEY_PLAIN, 2,(0, 255, 0), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(1)

