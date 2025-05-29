import requests
url = 'http://localhost:8000/test'

reponse = requests.get(url)
reponse = reponse.json()

print(reponse['message'])