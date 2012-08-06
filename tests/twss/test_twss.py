import os
import tempfile
import unittest
import twss
from twss import classifier

class TestTextClassifier(unittest.TestCase):

	def test_is_positive(self):
		result = twss.is_positive('That was not so hard')
		self.assertEquals(True, result)
		
		result = twss.is_positive('I am a normal sentance')
		self.assertEquals(False, result)
	
	def test_how_confident(self):
		probability = twss.how_confident('That was not so hard')
		self.assertTrue(probability >=0)
		self.assertTrue(probability <=1)
	
	def test_save_and_load(self):
		temp = tempfile.NamedTemporaryFile(delete=False)
		temp.close()
		
		twss.twss.save(temp.name)
		classifier = twss.classifier.TextClassifier.load(temp.name)
		
		result = classifier.is_positive('That was not so hard')
		self.assertEquals(True, result)
		
		result = classifier.is_positive('I am a normal sentance')
		self.assertEquals(False, result)
		os.unlink(temp.name)
