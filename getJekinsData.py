
# importing the requests library
import requests

# api-endpoint
URL = "https://jenkins-66e2ed6e-af76-40f4-a86b-b7cde6a06963.live.alta3.com/api/python?pretty=true"

# sending get request and saving the response as response object
r = requests.get(url = URL, auth = ('jarvis', 'alta3'),verify=False)
  
# extracting data in json format
data = r.json()
print(data)
