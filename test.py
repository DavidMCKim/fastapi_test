import json
import requests

url = 'http://localhost:8000/Items/'

data = {'name':'MCKIM', 'description':'test', 'price':2000, 'tax':0}

res = requests.post(url, data=json.dumps(data))

res.text
print(res.text)
print()