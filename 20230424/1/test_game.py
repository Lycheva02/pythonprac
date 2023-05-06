import unittest
from moodserver.__main__ import start_game
import moodclient.client as client
import asyncio
import socket
import multiprocessing
import time


class TestGame(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.proc = multiprocessing.Process(target=start_game)
		cls.proc.start()
		time.sleep(1)
		cls.pl = client.Client_Gameplay('moo')
	
	@classmethod
	def tearDownClass(cls):
		cls.pl.do_quit('')
		cls.proc.terminate()
	
	def test_0(self):
		self.pl.send_srv('addmon taxi WOW 23 1 1\n')
		ans = self.pl.socket.recv(1024).strip().decode()
		self.assertEqual(ans, 'moo added monster taxi to (1, 1) saying WOW with 23 hp')
	
	def test_1(self):
		self.pl.send_srv('move 1 0\n')
		ans = self.pl.socket.recv(1024)
		self.pl.send_srv('move 0 1\n')
		ans = self.pl.socket.recv(1024).strip().decode()
		ans = ans.split('\n')[1]
		self.assertEqual(ans, 'taxi WOW')
	
	def test_2(self):
		self.pl.send_srv('attack taxi 15\n')
		ans = self.pl.socket.recv(1024).strip().decode()
		tmplt = 'moo attacked taxi with spear, damage 15 hp\ntaxi now has 8'
		self.assertEqual(ans, tmplt)
