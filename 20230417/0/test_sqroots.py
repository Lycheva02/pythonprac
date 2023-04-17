import unittest
from unittest.mock import MagicMock, patch
import sqroots
import socket
import multiprocessing
import time

class TestSqroots(unittest.TestCase):
	
	def test_0_sqroots(self):
		self.assertEqual(sqroots.sqroots('1 2 1'), '-1.0')
	
	def test_1_sqroots(self):
		self.assertEqual(sqroots.sqroots('1 1 1'), '')
		
	def test_2_sqroots(self):
		self.assertEqual(sqroots.sqroots('1 0 -1'), '1.0 -1.0')
    
	def test_exception_sqroots(self):
		with self.assertRaises(BaseException):
			sqroots.sqroots('0 1 2')

class TestServer(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.proc = multiprocessing.Process(target=sqroots.serve)
		cls.proc.start()
		time.sleep(1)
	
	@classmethod
	def tearDownClass(cls):
		cls.proc.terminate()
		
	def setUp(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect(('127.0.0.1', 1337))
	
	def tearDown(self):
		self.s.close()
	
	def test_0_serve(self):
		self.assertEqual(sqroots.sqrootnet('1 2 1\n', self.s), '-1.0')
	
	def test_1_serve(self):
		self.assertEqual(sqroots.sqrootnet('1 1 1\n', self.s), '')
		
	def test_2_serve(self):
		self.assertEqual(sqroots.sqrootnet('1 0 -1\n', self.s), '1.0 -1.0')
