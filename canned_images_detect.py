# runs detector on successive images stored in a directory

import detector as dt
#import classifier as cl
import classifier_wRetraining as clwR
import time
import os

images_dir = '/home/ian/Desktop/test'

def main():
  # Creates graph from saved GraphDef.
  #cl.create_graph()
  clwR.load_graph()

  for file in sorted(os.listdir(images_dir), key=str.lower):
    if file.endswith(".jpg") or file.endswith(".JPG"):
      start = time.time() # want to time each cycle. starting stopwatch.
      full_file = os.path.join(images_dir, file)
      print(full_file)
      vote, target_label = dt.detector(full_file)
      print(target_label + ' is present.')
      
      end = time.time()
      print('Elapsed Time: ' + str(end - start)) # print out how long this detection cycle took
      
      print('********')

if __name__ == '__main__':
  main()
