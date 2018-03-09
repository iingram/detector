# runs detector on successive frames of a canned video

import cv2
from detector import *
import time

video_filename = 'test.mp4'

detections_count = 0 #currently only used if logging frames that detector marked as True

if __name__ == '__main__':
  camera = cv2.VideoCapture(video_filename)

  # Creates graph from saved GraphDef.
  create_graph()
  
  while(1):
    start = time.time() # want to time each cycle. starting stopwatch.
    num_throw_away_frames = 30 # simulate speed of classifier in real-time situation
    for i in xrange(num_throw_away_frames):
      retval, temp = camera.read()
    
    retval, camera_capture = camera.read()
    file = "test_image.png"
    cv2.imwrite(file, camera_capture)
    vote, target_label = detector('test_image.png')
    print(target_label + ' is present.')
    
    end = time.time()
    print('Elapsed Time: ' + str(end - start)) # print out how long this detection cycle took

    print('********')

    ### uncomment this section if you want to see the images that
    ### detector classified.  if you do invoke this section, loop will
    ### pause on each image till keystroke, ESC will quit the program
    #if(vote):
    #  cv2.circle(camera_capture,(320, 240), 50, (0,255,0), 5)
    #cv2.imshow('image', camera_capture)
    #k = cv2.waitKey(0)
    #if k == 27:         # wait for ESC key to exit
    #  cv2.destroyAllWindows()
    #  break
    ### end of optional image display section

    ### uncomment this section if you want the program to save all
    ### images for which detector has voted True
    #if(vote):
    #  detections_count += 1
    #  file = target_label + "_" + str(detections_count) + ".png"
    #  cv2.imwrite(file, camera_capture)
    ### end of optional image logging section
