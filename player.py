from __future__ import print_function
import sys


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):

        id = getattr(game_state, 'in_action')
        #if game_state('players')[0]
        print game_state
        
        return 500

    def showdown(self, game_state):
        pass
