import sys
from pic import Pic
from classifier import Classifier
from score import error

limit = int(sys.argv[1])
half = limit/2
data, targets = Pic.data(limit)
data = Pic.flatten(data)
data, cv_data = data[:half], data[half:]
targets, cv_targets = targets[:half], targets[half:]
preds = Classifier.predict(data, targets, data)
print error(preds, cv_targets)
#print preds
#print cv_targets
