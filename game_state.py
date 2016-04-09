from __future__ import print_function
import sys

NUMBERS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class GameState:
    def __init__(self,state):
        self.state = state

    def warning(self):
        print("WARNING: ", self.state, file=sys.stderr)

    def player(self):
        return self.state["players"][self.state[u"in_action"]]

    def get_cards(self):
        return self.player()[u"hole_cards"]

    def get_round(self):
        self.warning()
        return self.state[u"round"]

    def get_stack(self):
        return self.player()[u"stack"]

    def is_dealer(self):
        if self.state[u"in_action"][u"dealer"] == 1:
            return True
        return False

    def buy_in(self):
        return self.state["current_buy_in"]

    def keep(self):
        return self.buy_in() - self.player()["bet"]

    def get_rank(self):
        return self.get_cards()[u"rank"]

    def get_highest_rank(self):
        cards = self.get_cards()
        rank0 = cards[0][u"rank"]
        rank1 = cards[1][u"rank"]
        if (NUMBERS.index(rank0) > NUMBERS.index(rank1)):
            return rank0
        else:
            return rank1

    
    def community_cards(self):
        return self.state[u"community_cards"]

    def have_pair_in_hand(self):
        return self.get_cards()[0]["rank"] == self.get_cards()[1]["rank"]
