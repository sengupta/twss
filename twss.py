import nltk
import socket
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

def serve(PORT):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", PORT))
    server.listen(5)
    
    while True: 
        client_socket, client_address = server.accept()
        print "Got connection from ", client_address, "at ", datetime.datetime.now()
    
        client_test_statement = client_socket.recv(140)
        print "Got data: \n", client_test_statement
        if classifier.classify(extract_features(client_test_statement)): 
            client_socket.send("True")
            print ("True")
        else:
            client_socket.send("False")
            print ("False")
        client_socket.close()

serve(PORT)
