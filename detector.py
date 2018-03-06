# GOAL: given an image, a model, and a set of target labels,
# returns True if a criterion is met (such as: one of the target
# labels is the first in the list that the classifier returns), False
# if not

# right now just runs the classifier and returns True no matter what

from classifier import *

def detector(image):
  run_inference_on_image(image)
  return True




