class Team(object):
    """description of class"""

    def __init__(self, name):
        self.teamid = -1
        self.name = name

    def toString(cls):
        return cls.name