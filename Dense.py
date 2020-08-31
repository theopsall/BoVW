import sys 
import cv2 
import numpy as np 
from sklearn.cluster import KMeans
from Extractor import Extractor
# visual dictionary is also known as codebook

class DenseDetector():
    

    def __init__(self, step_size=20, feature_scale=20, img_bound=20) :

        
        self.initXyStep = step_size # size of the circle
        self.initFeatureScale = feature_scale # distance between the circles
        self.initImgBound = img_bound # Starting point from top left image corner
        
        
    def detect(self, img) :
        # Detect keypoints
        keypoints = []
        rows, cols = img.shape[:2]
        #self.initXyStep = int(rows/self.initFeatureScale)
        for x in range(self.initImgBound, rows, self.initFeatureScale):
            for y in range(self.initImgBound, cols, self.initFeatureScale):
                keypoints.append(cv2.KeyPoint(float(y), float(x), self.initXyStep))
        return keypoints
    


class Quantizer(object):
    
    def __init__(self, num_clusters=32):
        self.num_dims = 18
        self.extractor = Extractor('sift')
        self.num_clusters = num_clusters
        self.num_retries = 10 
        
    def quantize(self, datapoints):
        
        # mallon prepei na allaksw ta datapoints gia na ta dwsw ston kmeans !
        kmeans = KMeans(self.num_clusters)
        
        res = kmeans.fit(datapoints)
        
        centroids = res.cluster_centers_
        return kmeans, centroids
    
    def normalize(self, input_data):
        
        sum_input = np.sum(input_data)
        if sum_input > 0:
            return input_data / sum_input
        else :
            return input_data
    
    def get_feature_vector(self, kmeans, descriptors):
        im_features = np.array([np.zeros(self.num_clusters) 
                                for i in range(len(descriptors))])

        for i in range(len(descriptors)):

            for j in range(len(descriptors[i])):
                feature = descriptors[i][j]

                feature = feature.reshape(1,128)

                idx = kmeans.predict(feature)

                im_features[i][idx] += 1
        
        return im_features
    

class FeatureExtractor(object): 
    def extract_image_features(self, img): 
        # Dense feature detector 
        kps = DenseDetector().detect(img) 
 
        # SIFT feature extractor 
        kps, fvs = Extractor('sift').compute(img, kps) 
 
        return fvs 
 
    # Extract the centroids from the feature points 
    def get_centroids(self, input_map, num_samples_to_fit=10): 
        kps_all = [] 
 
        count = 0 
        cur_label = '' 
        for item in input_map: 
            if count >= num_samples_to_fit: 
                if cur_label != item['label']: 
                    count = 0 
                else: 
                    continue 
 
            count += 1 
 
            if count == num_samples_to_fit:  
                print("Built centroids for", item['label'])
 
            cur_label = item['label'] 
            img = cv2.imread(item['image']) 
            img = resize_to_size(img, 150) 
 
            num_dims = 128 
            fvs = self.extract_image_features(img) 
            kps_all.extend(fvs) 
 
        kmeans, centroids = Quantizer().quantize(kps_all) 
        return kmeans, centroids 
 
    def get_feature_vector(self, img, kmeans, centroids): 
        return Quantizer().get_feature_vector(img, kmeans, centroids) 
    
    
# Testing process 
if __name__ == "__main__" :
    input_img = cv2.imread("/home/theo/Desktop/bovw/SPECT/TRAIN/0/4sec_Athens Psyri Neighborhood Tour_cr1.png")
    input_img_dense = np.copy(input_img)
    #input_img_sift = np.copy(input_img)
    
    sift = Extractor('sift')
    keypoints = DenseDetector(20,20,0).detect(input_img_dense)
    print(len(keypoints))
    kp, des  = sift.compute(input_img, keypoints)
    
    q = Quantizer()
    kmeans, centroids = q.quantize(des)
    print(kmeans)
    print(centroids)
    print(len(centroids))
    input_img_dense = cv2.drawKeypoints(input_img_dense, keypoints,
                                        None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS )
    
    cv2.imshow('Dense ',input_img_dense)
 
    cv2.waitKey()
    """
    
    for imgs in 
    """
    
    
   