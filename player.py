from __future__ import print_function
import sys
import traceback
from game_state import GameState

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    traceback.print_exc()
    

class Player:
    VERSION = "Default Python folding player"
   
    def preFlopBet(self):
       if self.state.have_pair_in_hand():
          return 500
       else:
          return 0
 
    def calcBet(self):
        if self.state.get_round() == 0:
            return self.preFlopBet()
        elif self.state.get_round() == 1:
                if self.state.get_cards()[0] or self.state.get_cards()[1] in self.state.community_cards():
                    return self.state.keep()
                return self.keep()
        else:
            return self.state.keep()

    def betRequest(self, game_state):
        self.state = GameState(game_state)
        try:
            return self.calcBet()
        except Exception as x:
            warning("Exception during betRequest", x)
            return 501

    def showdown(self, game_state):
        pass
