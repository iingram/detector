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

#import classifier as cl
import classifier_wRetraining as clwR

target_filename = "example_target_file.txt"

with open(target_filename, 'r') as f:
  target_labels = [line.rstrip('\n') for line in f]

#target_labels = ['coffee mug', 'spatula']  # can you tell I am doing this in my kitchen?


def detector(image):
  #veryToppist = cl.run_inference_on_image(image)
  veryToppist = clwR.run_inference_on_image(image)

  # check for any of the target_labels in the category with highest
  # score from classifier.  provide label of match for use by apps.
  match = next((x for x in target_labels if x in veryToppist), False)
  if(match is False):
    return (False, "No target")
  else:
    return (True, match)





