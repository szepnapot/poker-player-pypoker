import unittest
from unittest import TestCase
from player import Player
from game_state import GameState
import json
#to run the test type into the command line:
# $ python -m unittest test_player

class GameStateMock( GameState ):
   pass


class TestPlayer(TestCase):
    
   def setUp(self):
      self.player = Player()
      json_string = open('pelda.json').read()
      self.pelda = json.loads(json_string)
      self.state = GameState(self.pelda)

   def test_keep(self):
      self.assertEqual(240, self.state.keep())

   def test_first_round(self):
      self.assertEqual(500,self.player.betRequest(self.pelda))

   def test_second_round(self):
      self.pelda[u"round"] = 1
      self.assertEqual(240,self.player.betRequest(self.pelda))
   
if __name__ == '__main__' :
   unittest.main()
