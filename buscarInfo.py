import requests
import json

def fetchData():
    r = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?itens=45')
    dictionary = json.loads(r.text)
    return dictionary

data = fetchData()