
# importing the requests library
import requests

# api-endpoint
URL = "http://0.0.0.0:2224/api/python?pretty=true"

# sending get request and saving the response as response object
r = requests.get(url = URL, auth = ('jarvis', '118183c729b6668877fc71c9d269ac7b13'),verify=False)
  
# extracting data in json format
data = r.json()
print(data)
