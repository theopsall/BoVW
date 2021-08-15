import numpy as np
from sklearn.cluster import MiniBatchKMeans

from BoVW.Extractor import Extractor

class BoVW(object):
    """
        Bag of Visual Words
    """

    def __init__(self, extractor="sift", num_clusters=32):
        self.num_dims = 18
        self.extractor = Extractor(extractor)
        self.num_clusters = num_clusters
        self.num_retries = 10

    def cluster(self, datapoints):

        kmeans = MiniBatchKMeans(self.num_clusters, init_size=3 * self.num_clusters + 100)

        res = kmeans.fit(datapoints)

        centroids = res.cluster_centers_
        return kmeans, centroids

    def get_feature_vector(self, kmeans, descriptors):
        im_features = np.array([np.zeros(self.num_clusters)
                                for i in range(len(descriptors))])

        for i in range(len(descriptors)):
            for j in range(len(descriptors[i])):
                feature = descriptors[i][j]
                feature = feature.reshape(1, 128)
                idx = kmeans.predict(feature)
                im_features[i][idx] += 1

        return im_features
