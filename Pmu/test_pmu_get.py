"""Unit test to get a file from the PMU web site"""
# importing the requests library
import requests


# api-endpoint
URL = "https://paris-sportifs.pmu.fr/event/654610"

# sending get request and saving the response as response object
RESPONSE = requests.get(url=URL)

print(RESPONSE)
