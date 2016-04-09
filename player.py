from __future__ import print_function
import sys


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            hand = game_state["players"][0]["PyPoker"]["hole_cards"]
            if "K" or "A" or "J" or "Q" or "A" in ["rank"]:
                return 600
            return 500
        except:
            return 500

    def showdown(self, game_state):
        pass
