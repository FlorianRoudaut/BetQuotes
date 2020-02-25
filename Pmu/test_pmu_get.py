"""Unit test to get a file from the PMU web site"""
# importing the requests library
import requests
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('/home/florian/Documents/Dev/BetQuotes/')

from WebScrapping.html_builder import build_html_tree

# api-endpoint
URL = "https://paris-sportifs.pmu.fr/event/669836"

# sending get request and saving the response as response object
RESPONSE = requests.get(url=URL)

PAGE = RESPONSE.text.replace("<%", "%").replace("%>", "%")
TREE = build_html_tree(PAGE)

NODES = TREE.get_element_by_attribute("data-name", '"sportif.clic.parier.sports.competition.match.cote"')


first_node = NODES[0]
sport= first_node.attributes["data-sport_id"]
competition= first_node.attributes["data-compet_id"]
event= first_node.attributes["data-event_id"]
event_split = event.split("__")
home_team = event_split[0]
away_team = event_split[2]

win = ""
draw = ""
lose = ""

for node in NODES:
    sort = node.attributes["data-sort"]
    if sort != '"MR"':
        continue
    if win == '':
        win = node.content
    elif draw == '':
        draw = node.content
    elif lose == '':
        lose = node.content

print(home_team)
print(away_team)
print(win)
print(draw)
print(lose)
