# twsslib.py

import datetime
import pickle
import os
import sys
import nltk

class TextClassifier:
    
    __module__ = os.path.splitext(os.path.basename(__file__))[0]
    
    def __init__(self, positive_filename, negative_filename):
            
        positive_data = open(positive_filename)
        negative_data = open(negative_filename)

	training_feature_set = []
	
	for line in positive_data:
	    features = self._extract_features(line)
	    training_feature_set.append((features, True))

        for line in negative_data: 
            features = self._extract_features(line)
            training_feature_set.append((features, False))

	self.classifier = nltk.NaiveBayesClassifier.train(training_feature_set)

	positive_data.close()
	negative_data.close()

    def _extract_features(self, phrase):
        """
        This function will extract features from the phrase being used. 
        Currently, the feature we are extracting are unigrams of the text corpus.
        """
        
        words = nltk.word_tokenize(phrase)
        features = {}
        for word in words:
            features['contains(%s)' % word] = (word in words)
        
        return features

    def is_positive(self, text):
        featureset = self._extract_features(text)
        return self.classifier.classify(featureset)
        
    def save(self, filename):
        ofile = open(filename,'w+')
        pickle.dump(self, ofile)
        ofile.close()
     
    @staticmethod     
    def load(filename):
        ifile = open(filename, 'r+')
        twss = pickle.load(ifile)
        ifile.close()
        return twss

def default_classifier():
	return TextClassifier.load('data/default_TextClassifier.pickle')

if __name__ == '__main__':
    twss = TextClassifier('data/twss.txt', 'data/non_twss.txt')
    print twss.is_positive("That was not so hard")
