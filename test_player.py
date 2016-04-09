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
      print 42
      self.state1()
      self.player = Player()
      self.state = GameState({'in_action':666})
      json_string = open('pelda.json').read()
      self.pelda = json.loads(json_string)

   def test_bet(self):
      self.assertEqual(500,self.player.betRequest({'in_action':666}))

   def test_first_round(self):
      self.assertEqual(500,self.player.betRequest(self.pelda))
   
   def state1(self):
      return {u'round': 105, u'bet_index': 5, u'current_buy_in': 40, u'orbits': 21, u'in_action': 2, u'minimum_raise': 20, u'big_blind': 40, u'dealer': 4, u'tournament_id': u'56fb8fc6364b600003000004', u'players': [{u'id': 0, u'version': u'Default Ruby folding player', u'bet': 0, u'stack': 0, u'status': u'out', u'name': u'RoyalRuby'}, {u'id': 1, u'version': u'Default Java folding player', u'bet': 0, u'stack': 0, u'status': u'out', u'name': u'Good Dolphin'}, {u'id': 2, u'version': u'ChecknRaise', u'bet': 20, u'hole_cards': [{u'suit': u'spades', u'rank': u'A'}, {u'suit': u'clubs', u'rank': u'9'}], u'stack': 2648, u'status': u'active', u'name': u'PyPoker'}, {u'id': 3, u'version': u'Default Java kick-ass player', u'bet': 0, u'stack': 0, u'status': u'out', u'name': u'DROP TABLE Students'}, {u'id': 4, u'version': u'Default C# folding player', u'bet': 40, u'stack': 2292, u'status': u'active', u'name': u'SmartFox'}], u'community_cards': [], u'pot': 60, u'game_id': u'5708cc06dfae79000300011d', u'small_blind': 20} 

if __name__ == '__main__' :
   unittest.main()
