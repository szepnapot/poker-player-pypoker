from __future__ import print_function
import sys


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    

class Player:
    VERSION = "Default Python folding player"

    def in_action_number(self, game_state):
        return game_state["in_action"]

    def player(self, game_state):
        return game_state["players"][self.in_action_number( game_state)]

    def get_cards(self, game_state):
        return game_state[self.player( game_state)]["hole_cards"]

    def get_stack(self, game_state):
        return game_state[self.player( game_state)]["stack"]

    def is_dealer(self, game_state):
        if game_state["in_action"]["dealer"] == 1:
            return True
        return False

    def community_cards(self, game_state):
        return game_state["in_action"]["community_cards"]

    def buy_in(self, game_state):
        return ""

    def betRequest(self, game_state):
        try:
            hand = self.get_cards( game_state )
            current_stack = self.get_stack( game_state )
            if "K" or "A" or "J" or "Q" or "A" in hand["rank"]:
                return 600
        except:
            return 500

    def showdown(self, game_state):
        pass

