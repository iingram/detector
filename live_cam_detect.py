# runs detector on successive images captured from webcam 

import cv2
import detector as dt
#import classifier as cl
import classifier_wRetraining as clwR
import time

CAMERA_PORT = 0
DETECTIONS_COUNT = 0 #currently only used if logging frames that detector marked as True

if __name__ == '__main__':
  
  camera = cv2.VideoCapture(CAMERA_PORT)

  # solves a bug where camera's auto-exposure won't have taken action
  # until after a healthy number of frames have been captured
  ramp_frames = 30
  for i in xrange(ramp_frames):
    retval, temp = camera.read()
  ### end camera "warm-up" section

  # Creates graph from saved GraphDef.
  #cl.create_graph()
  clwR.load_graph()
  
  while(1):
    start = time.time() # want to time each cycle. starting stopwatch.

    # these next three lines take a set of throw-away frames as this
    # hack gets camera caught up to the present (I think some buffer
    # in the camera is involved) and improves responsiveness of our
    # detection (i.e. much less latency between object entering frame
    # and this program saying it is there).  Obviously a performance
    # hit but it we are still within 1 Hz (on my machine).  6 frames
    # seemed to be just enough but further experiments could be done
    # to tweek this lower to maybe 4 or 5 but that is probably not
    # worth it while classification is taking 0.75 seconds
    num_throw_away_frames = 6
    for i in xrange(num_throw_away_frames):
      retval, temp = camera.read()

    retval, camera_capture = camera.read()
    file = "test_image.png"
    cv2.imwrite(file, camera_capture)
    vote, target_label = dt.detector('test_image.png')
    print(target_label + ' is present.')
    
    end = time.time()
    print('Elapsed Time: ' + str(end - start)) # print out how long this detection cycle took

    print('********')

    ### uncomment this section if you want to see the images that
    ### detector classified.
    #cv2.imshow('image', camera_capture) 
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:  # ESC to quit
    #  break
    # use following instead of preceding if you want to pause on each frame
    # until keystroke
    #k = cv2.waitKey(0)
    #if k == 27:         # wait for ESC key to exit
    #  break
    ### end of optional image display section

    ### uncomment this section if you want the program to save all
    ### images for which detector has voted True
    #if(vote):
    #  DETECTIONS_COUNT += 1
    #  file = target_label + "_" + str(DETECTIONS_COUNT) + ".png"
    #  cv2.imwrite(file, camera_capture)
    ### end of optional image logging section
cv2.destroyAllWindows()
cap.release()
