# Necessary imports
import numpy as np
import time
import sys
import os
import cv2

# Get webcam video
cap = cv2.VideoCapture(0)

# Initialize background filter
fsbg = cv2.BackgroundSubtractorMOG()

while(1):
    # Continually apply filter to camera
    ret, frame = cap.read()
    fgmask = fsbg.apply(frame)

    # Show results
    cv2.imshow('Frame', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
