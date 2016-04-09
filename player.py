from __future__ import print_function
import sys
from game_state import GameState

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    

class Player:
    VERSION = "Default Python folding player"
    
    def calcBet(self):
        if "K" or "A" or "J" or "Q" or "A" in self.state.get_rank():
            if self.state.get_round() == 0:
                return 500
            else:
                return 0
        else:
            return self.buy_in(self.game_state) - self.player()['bet']

    def betRequest(self, game_state):
        self.state = GameState(game_state)
        try:
            return self.calcBet()
        except:
            warning("EXCEPTION")
            return 500

    def showdown(self, game_state):
        pass

