# GOAL: given an image, a model, and a set of target labels,
# returns True if a criterion is met (such as: one of the target
# labels is the first in the list that the classifier returns), False
# if not

# target_label is now an argument.  not sure if this is quite how I
# want to do this as there is a sense that the each detector should be
# an encapsulated thing (target_labels and criterion/a).  One could
# argue that that suggests having a generic detector read from some
# sort of file that specifies the detector behavior but it might be
# unnecessarily complicated for our purposes to figure out to
# generalize/schematize detector criteria into such a schema.  Better
# probably to just keep it free and easy in the code of a detector.

# right now:
# - image is an argument
# - target label is an argument
# - model is hardcoded into classifier.py
# - detection criterion is: is the target label the very highest ranked prediction

from classifier import *


def detector(image, target_label):
  veryToppist = run_inference_on_image(image)
  if(target_label in veryToppist):
    return True
  else:
    return False




