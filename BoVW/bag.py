""" 
    Bag of Visual Words
"""

from  utilities import crawl_directory, load_data
from classifier import Classifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, f1_score
import Dense as grid
from Extractor import Extractor
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os 

def vstackDescriptors(descriptor_list):
    descriptors = np.array(descriptor_list[0])
    for descriptor in descriptor_list[1:]:
        descriptors = np.vstack((descriptors, descriptor)) 

    return descriptors




if __name__ == '__main__':
    train_path = "/home/theo/Desktop/bovw/SPECT/TRAIN"
    test_path = "/home/theo/Desktop/bovw/SPECT/TEST"
    tree = crawl_directory(test_path)
    data, labels = load_data(tree, img_type=0)
    

    #descriptors = []
    descriptors_list = [] 
    sift = Extractor('sift')
    for i, image in enumerate(data):
        #print("Image :",i)
        keypoints = grid.DenseDetector(20, 20, 5).detect(image)
        kp, des = sift.compute(image, keypoints)
        #print(len(kp))
        descriptors_list.append(des)
        #descriptors.extend(des)
    #print(descriptors)
    descriptors = vstackDescriptors(descriptors_list)
    
    print("Starting Kmeans")
    k = [50, 100, 200, 500, 1000, 2000]
    for num_cluster in k:
        print("Num of Clusters: {0}".format(num_cluster))
        quantinizer = grid.Quantizer(num_clusters=num_cluster)
        print("Initiliaze quantinizer")
        kmeans, centroids =quantinizer.quantize(descriptors)
        print("Kmeans finished")
        x = quantinizer.get_feature_vector(kmeans,descriptors_list)
        print("Features Extracted")
        print("SVM Classifier for kmeans with {0} number of clusters.".format(num_cluster))
        classifier = OneVsRestClassifier(LinearSVC())
        classifier.fit(x, labels)
        y = classifier.predict(x)
        print(y)
        break
    
    
    