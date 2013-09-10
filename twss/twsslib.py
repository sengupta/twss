import os
import sys
import nltk
import pickle
import datetime

class TWSS: 
    training_data = [] # [("sentence 1", bool), ("sentence 2", bool), ... ]
    classifier = None

    def __init__(self, sentence=None, training_data=None, positive_corpus_file=None, negative_corpus_file=None):
        if training_data:
            self.training_data = training_data
        if positive_corpus_file and negative_corpus_file: 
            self.import_training_data(positive_corpus_file, negative_corpus_file)
        if sentence: 
            self.__call__(sentence)

    def __call__(self, phrase):
        if not self.classifier: 
            self.train()
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

        # for line in positive_corpus: 
        #     self.training_data.append((line, True))

        # for line in negative_corpus: 
        #     self.training_data.append((line, False))

        # The following code works. Need to profile this to see if this is an
        # improvement over the code above. 
        positive_training_data = map(lambda x: (x, True), positive_corpus)
        negative_training_data = map(lambda x: (x, False), negative_corpus)
        self.training_data = positive_training_data + negative_training_data

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

