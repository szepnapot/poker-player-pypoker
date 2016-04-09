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

    def get_bet(self):
        pass

    def community_cards(self, game_state):
        return self.state["in_action"]["community_cards"]

 