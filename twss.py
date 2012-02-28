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

log = open('log.txt', 'a') 

class ServeTWSS(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(140)
        print "Got connection from: ", self.client_address[0]
        client_test_statement = self.data
        print "    Got data: ", client_test_statement
        log.write(self.client_address[0] + ", " + str(datetime.datetime.now()) + ", " + "\"" + client_test_statement + "\"" + ", ")
        if classifier.classify(extract_features(client_test_statement)): 
            self.request.sendall("True")
            print "Classified True\n"
            log.write("True\n")
        else: 
            self.request.sendall("False")
            print "Classified False\n"
            log.write("False\n")
        log.flush()

def serve():
    server = SocketServer.TCPServer(("", PORT), ServeTWSS)
    server.serve_forever()

if __name__ == "__main__": 
    serve()

