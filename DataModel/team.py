"""Module of the team class"""


class Team(object):
    """Domain model of a team that will play games"""

    def __init__(self, name):
        self.teamid = -1
        self.name = name

    def to_string(self):
        """team to string"""
        return self.name
