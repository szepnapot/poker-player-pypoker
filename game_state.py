from __future__ import print_function
import sys

class GameState:
	def __init__(self,state):
		self.state = state

	def get_cards(self):
		return game_state["players"][0]["PyPoker"]["hole_cards"]

	def warning(self):
		print("WARNING: ", self.state, file=sys.stderr)
 