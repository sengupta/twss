import nltk
import SocketServer
import sys
import datetime
import twsslib

try: 
    PORT = int(sys.argv[1])
except (IndexError, NameError): 
    PORT = 8083

classifier = twsslib.default_classifier()

print classifier.is_positive("That was not so hard")

log = open('log.txt', 'a') 

class ServeTWSS(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(140)
        print "Got connection from: ", self.client_address[0]
        client_test_statement = self.data
        print "    Got data: ", client_test_statement
        log.write(self.client_address[0] + ", " + str(datetime.datetime.now()) + ", " + "\"" + client_test_statement + "\"" + ", ")
        if classifier.is_positive(client_test_statement): 
            self.request.sendall("True")
            print "Classified True\n"
            log.write("True\n")
        else: 
            self.request.sendall("False")
            print "Classified False\n"
            log.write("False\n")
        log.flush()

def serve(PORT):
    server = SocketServer.TCPServer(("", PORT), ServeTWSS)
    server.serve_forever()

if __name__ == "__main__": 
    print "Serving..."
    serve(PORT)

