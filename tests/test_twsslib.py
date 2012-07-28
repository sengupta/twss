import os
import tempfile
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
	
	def test_save_and_load(self):
		temp = tempfile.NamedTemporaryFile(delete=False)
		temp.close()
		
		self.classifier.save(temp.name)
		classifier = twsslib.TextClassifier.load(temp.name)
		
		result = classifier.is_positive('That was not so hard')
		self.assertEquals(True, result)
		
		result = classifier.is_positive('I am a normal sentance')
		self.assertEquals(False, result)
		os.unlink(temp.name)