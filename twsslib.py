# twsslib.py

import sys
import nltk
import pickle
import datetime

class TextClassifier:
    training_data = []
    classifier = None
    
    def __init__(self, positive_filename='twss', negative_filename=None):
        if negative_filename is None:
            negative_filename = 'non_' + positive_filename
            
        positive_data = open('%s.txt' %(positive_filename))
        negative_data = open('%s.txt' %(negative_filename))

        for line in positive_data: 
            self.training_data.append((line, True))

        for line in negative_data: 
            self.training_data.append((line, False))
            

    def extract_features(self, phrase):
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
        featureset = self.extract_features(text)
        return self.classifier.classify(featureset)
        
    def save(self):
        ofile = open('classifier.dump','w+')
        pickle.dump(self.classifier, ofile)
        ofile.close()
        
    def load(self):
        ifile = open('classifier.dump', 'r+')
        self.classifier = pickle.load(ifile)
        ifile.close()
        
    def train(self):
        training_feature_set = [(self.extract_features(line), label) 
                                    for (line, label) in self.training_data]
        self.classifier = nltk.NaiveBayesClassifier.train(training_feature_set)



if __name__ == '__main__':
    twss = TextClassifier(positive_filename='twss', negative_filename='non_twss')
    twss.train()
    print twss.is_positive("That was not so hard")
