"""Module of the quote class"""


class Quote(object):
    """Represents a quote for a game and bet at a given time """

    def __init__(self, bet, quoteTime, quoteValue):
        self.quoteid = -1
        self.bet = bet
        self.quote_time = quoteTime
        self.quote_value = quoteValue

    def to_string(self):
        """Quote to string"""
        ret = self.bet.toString()+"|"+str(self.quote_time.year)+
        ret = ret+"/"+str(self.quote_time.month)
        ret = ret+"/"+str(self.quote_time.day)+"|"+str(self.quote_value)
        return ret
