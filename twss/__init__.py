import os
import classifier

positive_filename = os.path.join(os.path.dirname(__file__), './data/twss.txt')
negative_filename = os.path.join(os.path.dirname(__file__), './data/non_twss.txt')

twss = classifier.TextClassifier(positive_filename, negative_filename)

def is_positive(text):
  return twss.is_positive(text)
