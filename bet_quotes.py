"""
Entry point to create quotes
"""

import datetime
from DataModel.Team import Team
from DataModel.League import League
from DataModel.Game import Game
from DataModel.Bet import Bet
from DataModel.Quote import Quote

print("Hello World!")

RACING = Team('Racing')
MUNSTER = Team('Munster')
CUP = League("ChampionsCup")

DATE = datetime.datetime(2019, 11, 24)

GAME = Game(RACING, MUNSTER, CUP, DATE)

DRAWWGAME = Bet(GAME, 'Draw')

QUOTE = Quote(DRAWWGAME, datetime.datetime(2019, 11, 22), 24.5)

print(QUOTE.toString())
