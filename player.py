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
       stack = self.state.get_stack()
       if self.state.have_pair_in_hand():
          return round(stack * 0.5)
       elif self.state.get_highest_rank() == "A":
          return round(stack * 0.4)
       elif self.state.get_highest_rank() == "K":
          return round(stack * 0.3)
       return 0
 
    def calcBet(self):
        if self.state.get_round() == 0:
            return self.preFlopBet()
        elif self.state.get_round() > 0:
                #if self.state.get_cards()[0] in self.state.community_cards() or self.state.get_cards()[1] in self.state.community_cards():
                if self.preFlopBet() != 0:
                    return self.state.keep()
                return 0
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
