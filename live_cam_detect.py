# runs detector on successive images captured from webcam 

import cv2
from detector import *

camera_port = 0 
camera = cv2.VideoCapture(camera_port)

# this section solves a bug where camera's auto-exposure
# won't have taken action until after a healthy number of frames have
# been captured
ramp_frames = 30
def get_image():
  retval, im = camera.read()
  return im

for i in xrange(ramp_frames):
  temp = get_image()
### end camera "warm-up" section
  
if __name__ == '__main__':
  # Creates graph from saved GraphDef.
  create_graph()
  
  while(1):
    camera_capture = get_image()
    file = "test_image.png"
    cv2.imwrite(file, camera_capture)
    vote = detector('test_image.png')
    print('Vote is ' + str(vote))
    print('********')


