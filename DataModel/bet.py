"""Module of the bet class"""


class Bet:
    """Domain model for a type of bet, on a specific game"""
    def __init__(self, game, event):
        self.betid = -1
        self.game = game
        self.event = event

    def to_string(self):
        """Domain model for a type of bet"""
        return self.game.toString()+"|"+self.event
