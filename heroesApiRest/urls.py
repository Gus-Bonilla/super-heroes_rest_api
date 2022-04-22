from django.urls import path
from .views import RandomHeroDetailView
from .views import HelloWorldView

urlpatterns = [
    path("random-hero/", RandomHeroDetailView.as_view(), name='random_hero'),
    path("hello-world/", HelloWorldView.as_view(), name='hello_world'),
]