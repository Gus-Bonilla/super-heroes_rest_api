from django.views import View
from .models import Hero
from .models import HelloWorld
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .services import get_random_hero

# Create your views here.

class RandomHeroDetailView(View):
    def get(self, request):
        randomHeroObj = get_random_hero()
        return JsonResponse(model_to_dict(randomHeroObj))

class HelloWorldView(View):
    def get(self, request):
        helloWorldObj = HelloWorld()
        helloWorldObj.id = 1
        helloWorldObj.text = "Hello World!!"
        return JsonResponse(model_to_dict(helloWorldObj))
