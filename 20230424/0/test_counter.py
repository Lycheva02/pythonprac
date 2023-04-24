import unittest
from counter import fun


class TestCounter(unittest.TestCase):
	
	def test_0_counter(self):
		self.assertEqual(fun('a s d s'), "Введено 4 слова")
