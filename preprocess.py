import os
import re
from pic import Pic
from PIL import Image
import ImageFilter
import numpy

class Resize:

    @classmethod
    def resize(cls, pic):
        width, height = 38, 60
        return pic.resize((width, height), Image.ANTIALIAS)

    @classmethod
    def contour(cls, pic):
        return pic.filter(ImageFilter.CONTOUR)

    @classmethod
    def band(cls, pic):
        r, g, b = pic.split()
        return Image.merge("RGB", (g,g,g))

    @classmethod
    def crop(cls, pic, start_x, start_y, width, height):
        box = (start_x, start_y, start_x + width, start_y + height)
        return pic.crop(box)

    @classmethod
    def crop_to_avg_proportion(cls, limit):
        directory = "./data/train"
        _, _, _, _, avg_height, avg_width = Pic.size_ranges(limit)
        avg_proportion = avg_height/avg_width
        pics = []
        names = []
        for image in os.listdir(directory)[:limit]:
            filepath = directory + "/" + image
            pic = Image.open(filepath)
            numpy_pic = numpy.asarray(pic)
            height, width, _ = numpy_pic.shape

            new_height = width * avg_proportion
            new_width = height * (avg_width/avg_height)
            height_on_both_sides = int(round((height - new_height)/2))
            width_on_both_sides = int(round((width - new_width)/2))
            name = re.findall('/.*/.*(/.*)', pic.filename)[0]
            names.append(name)
            if new_height < height:
                pic = Resize.crop(pic, 0, height_on_both_sides, width, height-(2*height_on_both_sides))
            elif new_width < width:
                pic = Resize.crop(pic, width_on_both_sides, 0, width-(2*width_on_both_sides), height)
            else:
                print 'error'

            pics.append(pic)
        return pics, names


def apply_to_all(new_directory, method, limit=None):
    old_directory = "./data/train"
    for image in os.listdir(old_directory)[:limit]:
        # get the image
        filepath = old_directory + "/" + image
        pic = Image.open(filepath)
        pic = getattr(Resize, method)(pic)
        pic.save(new_directory + "/" + image)



if __name__ == "__main__":
    #apply_to_all('./test', 'crop_to_avg_proportion', limit=10)
    #print Pic.size_ranges(2000)
    pics, names = Resize.crop_to_avg_proportion(800)
    new_directory = './crop_band'
    for i,pic in enumerate(pics):
        name = names[i]
        filename = new_directory + name
        pic = Resize.resize(pic)
        pic = Resize.band(pic)
        pic.save(filename)
