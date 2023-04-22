import unittest
from unittest.mock import patch, MagicMock
import moodclient.client as client
import sys
import socket
from io import StringIO


class TestClient(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.mock_socket = MagicMock(spec=socket.socket)
		cls.mock_socket.send.return_value = cls.mock_socket
		socket.socket = MagicMock(return_value=cls.mock_socket)
		cls.clnt = client.Client_Gameplay('moo')
	
	@classmethod
	def TearDownClass(cls):
		cls.clnt.do_quit('')
	
	def test_0(self):
		mock_input = MagicMock(side_effect=['left', 'right'])
		while True:
			try:
				self.clnt.onecmd(mock_input())
			except:
				break
		self.assertEqual(self.mock_socket.send.call_count, 3)
		expected_calls = [
			unittest.mock.call('login moo\n'.encode()),
			unittest.mock.call('move -1 0\n'.encode()),
			unittest.mock.call('move 1 0\n'.encode())
		]
		self.mock_socket.send.assert_has_calls(expected_calls)
	
	def test_1(self):
		mock_input = MagicMock(side_effect=['left 2'])
		with patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.clnt.onecmd(mock_input())
			assert mock_stdout.getvalue() == 'Invalid arguments\n'
			self.assertEqual(self.mock_socket.send.call_count, 3)
	
	def test_2(self):
		mock_input = MagicMock(side_effect=['addmon taxi hello WOW hp 23 coords 1 1', 'addmon tux hp 23 coords 1 1 hello oooo'])
		while True:
			try:
				self.clnt.onecmd(mock_input())
			except:
				break
		self.assertEqual(self.mock_socket.send.call_count, 5)
		expected_calls = [
			unittest.mock.call('login moo\n'.encode()),
			unittest.mock.call('move -1 0\n'.encode()),
			unittest.mock.call('move 1 0\n'.encode()),
			unittest.mock.call('addmon taxi WOW 23 1 1\n'.encode()),
			unittest.mock.call('addmon tux oooo 23 1 1\n'.encode())
		]
		self.mock_socket.send.assert_has_calls(expected_calls)
