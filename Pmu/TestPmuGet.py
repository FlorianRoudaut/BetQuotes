# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://paris-sportifs.pmu.fr/event/654610"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 

print(r)