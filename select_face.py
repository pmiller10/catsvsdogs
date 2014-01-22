from preprocess import Resize
from sklearn.linear_model import LinearRegression
import numpy
from pic import Pic
import pdb

class Face:

    sections = 4

    def __init__(self):
        self.model = LinearRegression()

    def about_equal(self, x, y, error):
        return (x-y) < error

    def segments(self, pic):
        # break up image into 9 sub pictures 
        numpy_pic = numpy.asarray(pic)
        height, width, _ = numpy_pic.shape
        section_height, section_width = height/self.sections, width/self.sections
 
        current_bottom, current_right = 0, 0
        outers, centers = [], []
        print 'height ', height
        print 'width ', width
        while current_bottom <= height:
            while current_right <= width:
                # get the row
                crop = Resize.crop(pic, current_right, current_bottom, section_width*2, section_height*2)
	 
                dist_from_current_right_to_edge = width - ((2*section_width) + current_right)
                dist_from_current_bottom_to_edge = height - ((2*section_height) + current_bottom)
                #pdb.set_trace()
 
                dist_from_current_left_to_edge = current_right
                dist_from_current_top_to_edge = current_bottom
 
                print "dist_from_current_left_to_edge ", dist_from_current_left_to_edge 
                print "dist_from_current_right_to_edge ", dist_from_current_right_to_edge 
                if self.about_equal(dist_from_current_left_to_edge, dist_from_current_right_to_edge, section_width) and self.about_equal(dist_from_current_top_to_edge, dist_from_current_bottom_to_edge, section_height):
                    centers.append(crop)
                else:
                    outers.append(crop)
                current_right += section_width
                print current_right, current_bottom
            else:
                current_right = 0

            current_bottom += section_height

        return centers, outers
       
        def all_segments(self, pics):
            all_centers, all_outers = [], []
            for pic in pics:
                centers, outers = self.segments(pic)
                all_centers.append(centers)
                all_outers.append(outers)
            return all_centers, all_outers

        def train(self, pics):
            faces, non_faces = self.all_segments(pics)
            targets = []
            for f in faces:
                targets.append(1)
            for n in non_faces:
                targets.append(0)
            data = faces + non_faces

            model = self.model.fit(data, targets)
            self.model = model

        def find_face(self, pic):
            segments = self.segments(pic)
            preds = []
            for s in segments:
                preds.append(self.model.predict(s))

            highest = sorted(preds)[-1]
            index = preds.index(highest)
            return segments[index]

def test_segments():
    data = Pic.images(1)
    face = Face()
    print type(data[0])
    inners, outers = face.segments(data[0])
    print len(inners), len(outers)

if __name__ == "__main__":
    test_segments()
