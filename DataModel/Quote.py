class Quote(object):
    """Represents a quote for a game and bet at a given time """

    def __init__(self, bet, quoteTime, quoteValue):
        self.quoteid = -1
        self.bet = bet
        self.quoteTime = quoteTime
        self.quoteValue = quoteValue

    def toString(cls):
        return cls.bet.toString()+"|"+str(cls.quoteTime.year)+"/"+str(cls.quoteTime.month)+"/"+str(cls.quoteTime.day)+"|"+str(cls.quoteValue)

