from unittest import TestCase
from player import Player
from game_state import GameState
import json
#to run the test type into the command line:
# $ python -m unittest test_player

#class GameStateMock( GameState ):



class TestPlayer(TestCase):
    
   def setUp(self):
      self.player = Player()
      self.state = GameState({'in_action':666})
      json_string = open('pelda.json').read()
      self.pelda = json.loads(json_string)

   def test_bet(self):
      self.assertEqual(500,self.player.betRequest({'in_action':666}))

   def test_first_round(self):
      self.assertEqual(500,self.player.betRequest(self.pelda))
