import os
import re
from PIL import Image
import numpy

class Pic:

    @classmethod
    def data(self, limit=None):
        pics = []
        targets = []
        directory = "./data/train"
        for image in os.listdir(directory)[:limit]:
            # get the image
            filepath = directory + "/" + image
            pic = Image.open(filepath)
            pic = numpy.asarray(pic)
            pics.append(pic)

            # figure out if it's a cat or dog
            cat_or_dog = 0 if re.match('cat', image) else 1
            targets.append(cat_or_dog)
        return pics, targets

if __name__ == "__main__":
    d,t = Pic.data(10)
