from __future__ import print_function
import sys
from game_state import GameState

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    

class Player:
    VERSION = "Default Python folding player"
    

    def betRequest(self, game_state):
        state = GameState(game_state)
        try:
            return state.bet()
        except:
            return 500

    def showdown(self, game_state):
        pass

