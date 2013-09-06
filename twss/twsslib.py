import os
import sys
import nltk
import pickle
import datetime

class TWSS: 
    training_data = [] # [("sentence 1", bool), ("sentence 2", bool), ... ]
    classifier = None

    def __init__(self, positive_corpus_file=None, negative_corpus_file=None):
        if not self.classifier: 
            self.train()

    def __call__(self, phrase):
        print self.is_twss(phrase)

    def import_training_data(self,
            positive_corpus_file=os.path.join(os.path.dirname(__file__),
                "positive.txt"),
            negative_corpus_file=os.path.join(os.path.dirname(__file__),
                "negative.txt")
            ):
        """
        This method imports the positive and negative training data from the
        two corpus files and creates the training data list. 
        """

        positive_corpus = open(positive_corpus_file)
        negative_corpus = open(negative_corpus_file)

        for line in positive_corpus: 
            self.training_data.append((line, True))

        for line in negative_corpus: 
            self.training_data.append((line, False))

    def train(self): 
        """
        This method generates the classifier. This method assumes that the
        training data has been loaded
        """
        if not self.training_data: 
            self.import_training_data()
        training_feature_set = [(self.extract_features(line), label) 
                                    for (line, label) in self.training_data]
        self.classifier = nltk.NaiveBayesClassifier.train(training_feature_set)

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

    def is_twss(self, phrase):
        """
        The magic function- this accepts a phrase and tells you if it
        classifies as an entendre
        """
        featureset = self.extract_features(phrase)
        return self.classifier.classify(featureset)

    def save(self, filename='classifier.dump'):
        """
        Pickles the classifier and dumps it into a file
        """
        ofile = open(filename,'w+')
        pickle.dump(self.classifier, ofile)
        ofile.close()
        
    def load(self, filename='classifier.dump'):
        """
        Unpickles the classifier used
        """
        ifile = open(filename, 'r+')
        self.classifier = pickle.load(ifile)
        ifile.close()

