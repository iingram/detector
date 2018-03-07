# GOAL: given an image, a model, and a set of target labels,
# returns True if a criterion is met (such as: one of the target
# labels is the first in the list that the classifier returns), False
# if not

# right now:
# - image is an argument
# - target label is hardcoded
# - detection criterion is: is the target label the very highest ranked prediction

from classifier import *

target_label = 'coffee mug'

def detector(image):
  veryToppist = run_inference_on_image(image)
  if(target_label in veryToppist):
    return True
  else:
    return False




