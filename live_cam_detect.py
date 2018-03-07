# runs detector on successive images captured from webcam 

import cv2
from detector import *

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
    retval, camera_capture = camera.read()
    file = "test_image.png"
    cv2.imwrite(file, camera_capture)
    vote = detector('test_image.png')
    print('Vote is ' + str(vote))
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

