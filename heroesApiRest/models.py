from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=15)


class Hero(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    pictureURL = models.CharField(max_length=100)
    copyright = models.CharField(max_length=15, default="© 2022 MARVEL")