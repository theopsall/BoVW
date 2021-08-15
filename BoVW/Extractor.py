import cv2


class Extractor:

    def __init__(self, type_extractor):
        self.extractor = self.__extractor(type_extractor)

    def __extractor(self, type_extractor):

        if type_extractor == 'sift':
            return cv2.xfeatures2d.SIFT_create()
        elif type_extractor == 'surf':
            try:
                return cv2.xfeatures2d.SURF_create()
            except:
                raise Exception(
                    "In order to use SURF you have to install opencv from source with OPENCV_ENABLE_NONFREE option")

        elif type_extractor == 'orb':
            return cv2.ORB_create()
        else:
            raise Exception("Wrong extractor")

    def compute(self, img, kps):
        # compute descriptors and keypoints
        if img is None:
            print("Not a valid Image")
            raise TypeError
        if kps is None:
            print("Not a valid set of keypoints")
            raise TypeError

        kp, des = self.extractor.compute(img, kps)
        return kp, des
