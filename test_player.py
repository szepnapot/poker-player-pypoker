import unittest
from unittest import TestCase
from player import Player
from game_state import GameState
import json
#to run the test type into the command line:
# $ python -m unittest test_player

class TestPlayer(TestCase):
    
   def setUp(self):
      self.player = Player()
      json_string = open('pelda.json').read()
      self.pelda = json.loads(json_string)
      self.state = GameState(self.pelda)
   
   def test_preflop(self):
      self.assertEqual(False, self.state.is_preflop())

   def test_keep(self):
      self.assertEqual(240, self.state.keep())

   def test_first_round(self):
      self.assertEqual(500,self.player.betRequest(self.pelda))

   def test_first_round_nopair_a(self):
      self.pelda["players"][1]["hole_cards"][0]["rank"] = "A"
      self.assertEqual(400,self.player.betRequest(self.pelda))

   def test_second_round(self):
      self.pelda[u"bet_index"] = 1
      self.assertEqual(240,self.player.betRequest(self.pelda))
   
   def test_JJ_preflop(self):
      state = json.loads(open('prefloptest.json').read())
      self.assertEqual(500, self.player.betRequest(state)) 

   def test_get_highest_rank(self):
      self.state = GameState(self.pelda)
      self.assertEqual('K',self.state.get_highest_rank())
      self.pelda["players"][1]["hole_cards"][0]["rank"] = "A"
      self.assertEqual('A',self.state.get_highest_rank())
      self.pelda["players"][1]["hole_cards"][0]["rank"] = "7"
      self.assertEqual('K',self.state.get_highest_rank())
      self.pelda["players"][1]["hole_cards"][1]["rank"] = "J"
      self.assertEqual('J',self.state.get_highest_rank())
   
   def test_if_we_have_pairs(self):
      self.state = GameState(self.pelda)
      self.assertTrue(self.state.have_pair_in_hand())

   def test_in_command(self):
      assert( {u'rank': u'4', u'suit': u'spades'} in [ {u'rank': u'4', u'suit': u'spades'} ] )
      assert( not {u'rank': u'4', u'suit': u'spades'} in [ {u'rank': u'4', u'suit': u'hearts'} ] )

if __name__ == '__main__' :
   unittest.main()
