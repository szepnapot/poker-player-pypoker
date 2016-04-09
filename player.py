from __future__ import print_function
import sys
import traceback
from game_state import GameState

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    traceback.print_exc()
    

class Player:
    VERSION = "Default Python folding player"
    
    def calcBet(self):
        if self.state.get_round() == 0:
            if "K" or "A" or "J" or "Q" or "A" in self.state.get_rank():
                return 500
            else:
                return 0
        else:
            return self.state.buy_in() - self.state.player()['bet']

    def betRequest(self, game_state):
        self.state = GameState(game_state)
        try:
            return self.calcBet()
        except Exception as x:
            warning("Exception during betRequest", x)
            return 501

    def showdown(self, game_state):
        pass

