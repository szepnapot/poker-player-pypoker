from __future__ import print_function
import sys

class GameState:
    def __init__(self,state):
        self.state = state

    def warning(self):
        print("WARNING: ", self.state, file=sys.stderr)

    def player(self):
        return self.state["players"]["in_action_number"]

    def get_cards(self):
        return self.player()["hole_cards"]

    def get_stack(self):
        return self.player()["stack"]

    def is_dealer(self):
        if self.state["in_action"]["dealer"] == 1:
            return True
        return False
    def get_rank(self):
        return self.get_cards()["rank"]
    
    def get_bet(self):
        if "K" or "A" or "J" or "Q" or "A" in self.get_rank():
            if game_state['round'] == 0:
                return 500
            else:
                return 0
        else:
            return self.buy_in(self.game_state) - self.player()['bet']

    def community_cards(self, game_state):
        return self.state["in_action"]["community_cards"]

 
