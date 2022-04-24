import unittest
from django.test import Client

class ViewsTestCase(unittest.TestCase):
    client = Client()

    def test_randomHeroDetailView(self):
        url = "/heroes-api/random-hero/"
        response = self.client.get(url)
        responseJSON = response.json()
        self.assertEqual(responseJSON["id"], 1)

    def test_helloWorldView(self):
        url = "/heroes-api/hello-world/"
        response = self.client.get(url)
        responseJSON = response.json()
        self.assertEqual(responseJSON["id"], 1)
        self.assertEqual(responseJSON["text"], "Hello World!!")


if __name__ == '__main__':
    unittest.main()
