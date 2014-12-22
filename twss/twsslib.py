import io
import os
import pickle
import nltk
import sys


class TWSS(object):
    training_data = []  # [("sentence 1", bool), ("sentence 2", bool), ... ]
    classifier = None

    def __init__(self, sentence=None, training_data=None,
                 positive_corpus_file=None, negative_corpus_file=None):
        if training_data is not None:
            self.training_data = training_data
        if positive_corpus_file is not None and \
           negative_corpus_file is not None:
            self.import_training_data(positive_corpus_file,
                                      negative_corpus_file)
        if sentence is not None:
            self(sentence)  # Don't call __call__ on instance.

    def __call__(self, phrase):
        if not self.classifier:
            self.train()
        return self.is_twss(phrase)

    def import_training_data(self, positive_corpus_file=None,
                             negative_corpus_file=None):
        """
        This method imports the positive and negative training data from the
        two corpus files and creates the training data list.
        """

        if positive_corpus_file is None:
            positive_corpus_file = os.path.join(os.path.dirname(__file__),
                                                "positive.txt")
        if negative_corpus_file is None:
            negative_corpus_file = os.path.join(os.path.dirname(__file__),
                                                "negative.txt")

        # map() with lambda is very unpythonic and slow. Some other
        # alternatives are:-
        # 1. Two list-comprhensions(LC).
        # 2. One LC followed by a extend.
        # 3. One LC followed by append calls(save .append in a local variable)
        # 4. Two generator expressions chained using itertools.chain().
        # Out of these the append one outperforms the extend one by a slight
        # margin for bigger data set, so that's the one I used here.

        # Nested with-statements to support Python 2.6 as well.
        with io.open(positive_corpus_file, 'rt') as positive_corpus:
            with io.open(negative_corpus_file, 'rt') as negative_corpus:
                self.training_data = [(x, True) for x in positive_corpus]
                training_data_append = self.training_data.append
                for x in negative_corpus:
                    training_data_append((x, False))

    def train(self):
        """
        This method generates the classifier. This method assumes that the
        training data has been loaded
        """
        if not self.training_data:
            self.import_training_data()

        extract_features = self.extract_features  # prevent unnecessary lookups
        training_feature_set = [(extract_features(line), label)
                                for (line, label) in self.training_data]
        self.classifier = nltk.NaiveBayesClassifier.train(training_feature_set)

    def extract_features(self, phrase):
        """
        This function will extract features from the phrase being used.
        Currently, the feature we are extracting are unigrams of the text
        corpus.
        """
        words = nltk.word_tokenize(phrase)
        features = {}
        for word in words:
            # Why not simply set it to True?
            features['contains(%s)' % word] = (word in words)
        return features

    def is_twss(self, phrase):
        """
        The magic function- this accepts a phrase and tells you if it
        classifies as an entendre
        """
        featureset = self.extract_features(phrase)
        return self.classifier.classify(featureset)

    def save(self, filename=None):
        """
        Pickles the classifier and dumps it into a file
        """
        if filename is None:
            filename = 'classifier.dump'

        with open(filename, 'wt+') as ofile:
            pickle.dump(self.classifier, ofile)

    def load(self, filename=None):
        """
        Unpickles the classifier used
        """
        if filename is None:
            filename = 'classifier.dump'

        with io.open(filename, 'rt+') as ifile:
            self.classifier = pickle.load(ifile)
