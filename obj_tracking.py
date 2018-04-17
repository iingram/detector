from detector import *
import numpy as np
import time

fgbg = cv2.createBackgroundSubtractorMOG()

images_dir = '/Users/Loaner/Dropbox/animalDetector/image_recognition_training/tf_files'

for file in sorted(os.listdir(images_dir), key=str.lower):
  if file.endswith(".jpg") or file.endswith(".JPG"):
    full_file = os.path.join(images_dir, file)
    image = imread(full_file, IMREAD_COLOR )
    fgmask = fgbg.apply(image)
    cv2.imshow('frame',fgmask)
    #imshow( "Display window", image );
    time.sleep(5)
    print('********')

cap.release()
cv2.destroyAllWindows()
