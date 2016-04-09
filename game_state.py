from __future__ import print_function
import sys

class GameState:
    def __init__(self,state):
        self.state = state

    def warning(self):
        print("WARNING: ", self.state, file=sys.stderr)

    def player(self):
        return self.state["players"][u"in_action"]

    def get_cards(self):
        return self.player()[u"hole_cards"][u"rank"]

    def get_round(self):
        self.warning()
        return self.state[u"round"]

    def get_stack(self):
        return self.player()[u"stack"]

    def is_dealer(self):
        if self.state[u"in_action"][u"dealer"] == 1:
            return True
        return False

    def get_rank(self):
        return self.get_cards()[u"rank"]
    
    def community_cards(self):
        return self.state[u"in_action"][u"community_cards"]

    def buy_in(self):
        return self.state[u"in_action"][u"current_buy_in"]
 
