import unittest
import random
from ..services import generateRequest
from ..services import get_random_hero
from ..models import Hero

class ServicesTestCase(unittest.TestCase):
    def test_generateRequest(self):
        url = "https://gateway.marvel.com:443/v1/public/characters"
        offset = str(random.randint(0, 1560))
        payload = {'orderBy': 'name', 'limit': '1', 'offset': offset, 'ts': '1',
                   'apikey': 'bba91db5f9c6865d7e903f5391dca74b',
                   'hash': 'c7ebb8b5440c9fdd1070dfd8899c9d64'}

        responseJSON = generateRequest(url, payload)
        self.assertIsNotNone(responseJSON)
        self.assertEqual(responseJSON["code"], 200)
        self.assertEqual(responseJSON["status"], "Ok")

    def test_getRandomHero(self):
        hero = get_random_hero()
        self.assertIsInstance(hero, Hero)
        self.assertEqual(hero.id, 1)


if __name__ == '__main__':
    unittest.main()
