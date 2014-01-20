from PIL import Image
import ImageFilter
import os

class Resize:

    @classmethod
    def resize(cls, pic):
        width, height = pic.size[0]/2, pic.size[1]/2
        return pic.resize((width, height), Image.ANTIALIAS)

    @classmethod
    def contour(cls, pic):
        return pic.filter(ImageFilter.CONTOUR)

    @classmethod
    def band(cls, pic):
        r, g, b = pic.split()
        return Image.merge("RGB", (g,g,g))

def apply_to_all(new_directory, method, limit=None):
    old_directory = "./data/train"
    for image in os.listdir(old_directory)[:limit]:
        # get the image
        filepath = old_directory + "/" + image
        pic = Image.open(filepath)
        pic = getattr(Resize, method)(pic)
        pic.save(new_directory + "/" + image)

if __name__ == "__main__":
    apply_to_all('./test', 'contour', limit=10)
