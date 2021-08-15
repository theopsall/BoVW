import cv2



# visual dictionary is also known as codebook

class DenseDetector:
    """
        Dense Detector parse image in grid.
    """

    def __init__(self, step_size=20, feature_scale=20, img_bound=20):

        self.initXyStep = step_size  # size of the circle
        self.initFeatureScale = feature_scale  # distance between the circles
        self.initImgBound = img_bound  # Starting point from top left image corner

    def detect(self, img):
        """Detects the keypoints of the image in grid
        Args:
            img (list): Image in Array
        Returns:
            keypoints [list]: Returns the Grid Keypoints of the image
        """
        # Detect keypoints
        keypoints = []
        rows, cols = img.shape[:2]
        # self.initXyStep = int(rows/self.initFeatureScale)
        for x in range(self.initImgBound, rows, self.initFeatureScale):
            for y in range(self.initImgBound, cols, self.initFeatureScale):
                keypoints.append(cv2.KeyPoint(float(y), float(x), self.initXyStep))
        return keypoints

