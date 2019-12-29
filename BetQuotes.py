import datetime
from DataModel.Team import Team
from DataModel.League import League
from DataModel.Game import Game
from DataModel.Bet import Bet
from DataModel.Quote import Quote

print("Hello World!")

racing = Team('Racing')
munster = Team('Munster')
cup = League("ChampionsCup")

date = datetime.datetime(2019, 11, 24)

game = Game(racing,munster,cup,date)

drawGame = Bet(game,'Draw')

quote = Quote(drawGame,datetime.datetime(2019, 11, 22),24.5)

print(quote.toString())