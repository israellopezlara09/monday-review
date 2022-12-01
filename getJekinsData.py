# importing the requests library
import requests
import json

# api-endpoint
URL = "https://jenkins-66e2ed6e-af76-40f4-a86b-b7cde6a06963.live.alta3.com/api/json?pretty=true"

# sending get request and saving the response as response object
r = requests.get(url = URL, auth = ('jarvis', '118183c729b6668877fc71c9d269ac7b13'),verify=False)
  
# extracting data in json format
data = json.loads(r.text)
print(data)
