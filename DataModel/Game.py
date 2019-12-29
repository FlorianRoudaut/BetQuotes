class Game(object):
    """description of class"""

    def __init__(self, hometeam, awayteam, league, date):
        self.gameid = -1
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.league = league
        self.date = date

    def toString(cls):
        return cls.hometeam.toString()+"|"+cls.awayteam.toString()+"|"+cls.league.toString()+"|"+str(cls.date.year)+"/"+str(cls.date.month)+"/"+str(cls.date.day)