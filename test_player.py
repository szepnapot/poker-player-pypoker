from unittest import TestCase
from player import Player
#to run the test type into the command line:
# $ python -m unittest test_player

class TestPlayer(TestCase):
	def setUp(self):
		self.player = Player()

	def test_bet(self):
		self.assertEqual(500,self.player.betRequest({"in_action":666}))

