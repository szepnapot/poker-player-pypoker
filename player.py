
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            hand = game_state["players"][0]["PyPoker"]["hole_cards"]
            return 500
        except:
            return 500

    def showdown(self, game_state):
        pass
