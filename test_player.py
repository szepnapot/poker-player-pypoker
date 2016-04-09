from unittest import TestCase
from player import Player
from game_state import GameState
#to run the test type into the command line:
# $ python -m unittest test_player

class TestPlayer(TestCase):
	def setUp(self):
		self.player = Player()
		self.state = GameState({'in_action':666})

	def test_bet(self):
		self.assertEqual(500,self.player.betRequest({'in_action':666}))

