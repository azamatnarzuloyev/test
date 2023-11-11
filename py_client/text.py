import requests

res = requests.get('http://127.0.0.1:8000/list-view/')
json = res.json()

print(json[1]['name'])

data  =  lambda x: print(x)

print(data(json))

