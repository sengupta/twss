import os
import unittest
import twsslib

class TestTextClassifier(unittest.TestCase):
	
	def setUp(self):
		positive = os.path.join(os.path.dirname(__file__), '../data/twss.txt')
		negative = os.path.join(os.path.dirname(__file__),  '../data/non_twss.txt')
		self.classifier = twsslib.TextClassifier(positive, negative)
		
	def test_is_positive(self):
		result = self.classifier.is_positive('That was not so hard')
		self.assertEquals(True, result)
		
		result = self.classifier.is_positive('I am a normal sentance')
		self.assertEquals(False, result)