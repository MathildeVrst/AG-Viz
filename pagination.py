import json
import requests

data_from_API = []
pagination = True
c = 0 

while pagination == True: 
    c = c+1
    param = {'page': c,}
    basic_url = 'https://anthologiagraeca.org/api/'
    endpoint = "passages"
    r = requests.get(basic_url + endpoint,param).json()
    if r['next'] is None:
        pagination = False
    for item in r['results']:
        data_from_API.append(item)
        
with open('dump_api.json', 'w') as f:
    json.dump(data_from_API, f)
