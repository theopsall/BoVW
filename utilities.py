""" Auxiliary file, with helper functions """
import numpy as np 
import os 
import cv2

import numpy as np 
from pandas import get_dummies, cut


def crawl_directory(directory) -> list:
    """Crawling data directory
        
        ------------------------------
        Parameters:
            directory (str) : The directory to crawl

        ------------------------------
        Returns:
            tree (list)     : A list with all the filepaths
           
    """
    tree = []
    subdirs = [folder[0] for folder in os.walk(directory)]

    for subdir in subdirs:
        files = next(os.walk(subdir))[2]
        for _file in files:
            tree.append(os.path.join(subdir, _file))
            
    return tree

def load_data(tree, img_type = 1) -> tuple :
    """Loading images and labels
    
        ------------------------------
        Parameters:
            tree (list)    : images directory
            img_type (int) : The way to read the images, 
                            0           : GrayScale
                            1 (Default) : Colored
                           -1           : Unchanged
        ------------------------------
        Returns:
            images (list)  : A list which includes all the loaded images as numpy arrays
            labels (list)  : A paired list to images, containig the label for each image
    """
    labels = []
    images = []
    
    for img in tree:
        # os.sep is the system's pathname seperator 
        labels.append(img.split(os.sep)[-2]) # with -2 we get the label, which is always one level before the file
        images.append(cv2.imread(img, img_type))
        

    return images, labels

def shuffling(images, labels) -> tuple :
    """Shuffling both images and label
    
        ------------------------------
        Parameters:
            images (list) : List with images
            labels (list) : List with labels, 
        
        ------------------------------
        Returns:
            images (list) : A shuffled list which includes all the loaded images as numpy arrays
            labels (list) : A paired list to images, containig the label for each image
    """
    
    c = list(zip(images, labels))
    np.random.shuffle(c)
    images, labels = zip(*c)
    
    
    return images, labels

def categorize_labels(labels) -> tuple: 
    
    for idx, _l in enumerate(set(labels)):
        print(idx, _l)
    
    #return categories 

if __name__ == '__main__':
    path = '/media/theo/Data/CIL/bovw/test_data/train'
    data = crawl_directory(path)
    #print(data)
    images, labels = load_data(data)
    #print(images)
    #print(labels)
    print(len(set(labels)))
    print(categorize_labels(labels))
    

    
