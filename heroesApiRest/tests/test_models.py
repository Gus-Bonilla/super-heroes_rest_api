import unittest
from .models_creator import create_helloWorld
from .models_creator import create_hero
from ..models import Hero
from ..models import HelloWorld

class ModelsTestCase(unittest.TestCase):
    def test_helloWorld_creation(self):
        helloW = create_helloWorld()
        self.assertTrue(isinstance(helloW, HelloWorld))

    def test_hero_creation(self):
        hero = create_hero()
        self.assertTrue(isinstance(hero, Hero))


if __name__ == '__main__':
    unittest.main()
