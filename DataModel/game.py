"""Module of the game class"""


class Game:
    """Domain model for a game between two teams"""

    def __init__(self, hometeam, awayteam, league, date):
        self.gameid = -1
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.league = league
        self.date = date

    def to_string(self):
        """Game to string"""
        ret = self.hometeam.toString()+"|"+self.awayteam.toString()+
        ret = ret + "|"+self.league.toString()
        ret = ret+"|"+str(self.date.year)+"/"+str(self.date.month)
        ret = ret+"/"+str(self.date.day)
        return ret
