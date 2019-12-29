class Bet(object):

    """description of class"""
    def __init__(self, game, event):
        self.betid = -1
        self.game = game
        self.event = event

    def toString(cls):
        return cls.game.toString()+"|"+cls.event