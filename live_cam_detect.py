# runs detector on successive images captured from webcam 

import cv2
from detector import *
import time

if __name__ == '__main__':
  camera_port = 0 
  camera = cv2.VideoCapture(camera_port)

  # solves a bug where camera's auto-exposure won't have taken action
  # until after a healthy number of frames have been captured
  ramp_frames = 30
  for i in xrange(ramp_frames):
    retval, temp = camera.read()
  ### end camera "warm-up" section

  # Creates graph from saved GraphDef.
  create_graph()
  
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
    vote = detector('test_image.png')
    print('Vote is ' + str(vote))
    
    end = time.time()
    print('Elapsed Time: ' + str(end - start)) # print out how long this detection cycle took

    print('********')

    ### uncomment this section if you want to see the images that
    ### detector classified.  if you do invoke this section, loop will
    ### pause on each image till keystroke, ESC will quit the program
    #cv2.imshow('image', camera_capture)
    #k = cv2.waitKey(0)
    #if k == 27:         # wait for ESC key to exit
    #  cv2.destroyAllWindows()
    #  break
    ### end of optional image display section

