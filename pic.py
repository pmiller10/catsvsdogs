import os
import re
from PIL import Image
import numpy
from copy import copy

#directory = "./data/train"
directory = "./test" # TODO don't hardcode this

class Pic:

    @classmethod
    def data(self, limit=None):
        pics = []
        targets = []
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

    @classmethod
    def resize(cls, pics, size):
        resized = []
        for pic in pics:
            pic = copy(pic)
            pic.resize(size)
            resized.append(pic)
        return resized

    @classmethod
    def flatten(cls, pics):
        flat = []
        for p in pics:
            flat.append(p.flatten())
        return flat

    @classmethod
    def size_ranges(cls, limit=None):
        """
        Get the largest, smallest sizes for each dimension.
        Find the narrowest/widest and shortest/tallest pictures.
        """
        narrowest, widest, shortest, tallest = 10000, 0, 10000, 0
        total_width, total_height = 0, 0
        for image in os.listdir(directory)[:limit]:
            filepath = directory + "/" + image
            pic = Image.open(filepath)
            pic = numpy.asarray(pic)
            height, width, _ = pic.shape
            total_width += width
            total_height += height
            if height > tallest:
                tallest = height
            elif height < shortest:
                shortest = height
            if width > widest:
                widest = width
            elif width < narrowest:
                narrowest = width
        return shortest, tallest, narrowest, widest, (total_height/float(limit)), (total_width/float(limit))


if __name__ == "__main__":
    print Pic.size_ranges(2000)
