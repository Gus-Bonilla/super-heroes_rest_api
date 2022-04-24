import requests
import random
from .models import Hero

def generateRequest(url, payload={}):
    response = requests.get(url, params=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_random_hero():
    offset = str(random.randint(0, 1560))
    payload = {'orderBy': 'name', 'limit': '1', 'offset': offset, 'ts': '1',
               'apikey': 'bba91db5f9c6865d7e903f5391dca74b',
               'hash': 'c7ebb8b5440c9fdd1070dfd8899c9d64'}

    response = generateRequest("https://gateway.marvel.com:443/v1/public/characters", payload)
    randomHeroObj = Hero()

    if response:
        randomHeroObj.id = 1
        randomHeroObj.copyright = response.get('copyright')
        randomHeroObj.name = response.get('data').get('results')[0].get('name')
        randomHeroObj.description = response.get('data').get('results')[0].get('description')
        randomHeroObj.pictureURL = response.get('data').get('results')[0].get('thumbnail').get('path')
        randomHeroObj.pictureURL = randomHeroObj.pictureURL + '.' + response.get('data').get('results')[0].get('thumbnail').get('extension')
        randomHeroObj.pictureURL = 'https' + randomHeroObj.pictureURL[4:]
    else:
        randomHeroObj.id = 0
        randomHeroObj.name = "Batman"
        randomHeroObj.description = "He is the VENGEANCE xD"
        randomHeroObj.pictureURL = "https://m.media-amazon.com/images/I/41AuNl6Yw9L._AC_.jpg"

    return randomHeroObj