# Necessary imports
import numpy as np
import time
import sys
import os
import cv2

CIRCLE_DIAMETER_PIXELS = 100

def findBrightestSpot(img):
    gray = cv2.GaussianBlur(img, (5, 5), 1)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    image = img.copy()
    cv2.circle(image, maxLoc, CIRCLE_DIAMETER_PIXELS, (255, 0, 0), 2)

    # display the results of our newly improved method
    cv2.imshow("Robust", image)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        return

def main():
    # Get webcam video
    cap = cv2.VideoCapture(0)

    # Initialize background filter
    fsbg = cv2.BackgroundSubtractorMOG()


    while(1):
        ret, frame = cap.read()
        fgmask = fsbg.apply(frame)
        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        findBrightestSpot(fgmask)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
  main()
