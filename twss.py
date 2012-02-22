import nltk
import SocketServer
import sys
import datetime

PORT = int(sys.argv[1])

def extract_features(phrase):
    """
    This function will extract features from the phrase being used. 
    Currently, the feature we are extracting are unigrams of the text corpus.
    """
    
    words = nltk.word_tokenize(phrase)
    features = {}
    for word in words:
        features['contains(%s)' % word] = (word in words)
    return features

twss_data = open('twss.txt')
non_twss_data = open('non_twss.txt')

training_data = []

for line in twss_data: 
    training_data.append((line, True))

for line in non_twss_data: 
    training_data.append((line, False))

training_feature_set = [(extract_features(line), label) for (line, label) in training_data]

classifier = nltk.NaiveBayesClassifier.train(training_feature_set)

print classifier.classify(extract_features("That was not so hard"))

class ServeTWSS(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(140)
        print "{} wrote:".format(self.client_address[0])
        print self.data
        if classifier.classify(extract_features(client_test_statement)): 
            self.request.sendall("True")
            print "True"
        else: 
            self.request.sendall("False")
            print "False"

server = SocketServe.TCPServer(("", PORT), ServeTWSS)
server.serve_forever()

