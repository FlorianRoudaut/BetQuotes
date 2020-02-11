"""Module of the league class"""


class League:
    """Domain model for a league, a competition between a set of teams"""

    def __init__(self, name):
        self.leagueid = -1
        self.name = name

    def to_tring(self):
        """League to string"""
        return self.name
