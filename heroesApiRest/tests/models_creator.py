from faker import Faker
from ..models import Hero
from ..models import HelloWorld

def create_helloWorld():
    fakeGen = Faker()
    text = fakeGen.name()
    return HelloWorld.objects.create(text=text)

def create_hero():
    fakeGen = Faker()
    name = fakeGen.name()
    description = fakeGen.text()
    pictureURL = fakeGen.address()
    copyright = fakeGen.name()
    return Hero.objects.create(name=name, description=description, pictureURL=pictureURL, copyright=copyright)