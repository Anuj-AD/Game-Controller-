import cv2
import numpy as np
import pyautogui as p
import time

cap = cv2.VideoCapture(0)
left = False
right = False
up = False
down = False
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    img2 = red
    red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(red, 110, 255, cv2.THRESH_BINARY)
    M = cv2.moments(threshold)
    
    if M["m00"] != 0.0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(threshold, (cX, cY), 5, (255, 255, 255), -1)
        if cX > 400 and left == False: 
          print('l')
          p.keyUp('down')
          p.keyUp('right')
          p.keyDown('up')
          p.keyDown('left')
          left = True
          right = False
          up = True
          down = False
        elif cX < 200 and right == False: 
          print('r')
          p.keyUp('down')
          p.keyUp('left')
          p.keyDown('up')
          p.keyDown('right')
          left = False
          right = True
          up = True
          down = False
        elif cX > 200 and cX <400:
          if up == False:
            print('u')
            p.keyDown('up')
          p.keyUp('down')
          p.keyUp('left')
          p.keyUp('right')
          left = False
          right = False
          up = True
          down = False
          
    elif down == False:
          print('d')
          p.keyUp('up')
          p.keyUp('left')
          p.keyUp('right')
          p.keyDown('down')
          left = False
          right = False
          up = False
          down = True
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", threshold)
    
    key = cv2.waitKey(1)
    if key == 27:
        break