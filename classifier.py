from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC




class Classifier:
    
    def __init__(self):
        self.classifier = OneVsRestClassifier(SVC()) 
    
    def fit(self, X, y):
        return self.classifier.fit(X,y)
        
    def predict(self, X):
        return self.classifier.predict(X) 
        
        
        