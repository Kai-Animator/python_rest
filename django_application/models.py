from django.db import models

# Create your models here.

class Cowboys(models.Model):
    name = models.CharField(max_lenght=32, unique=True, null=False)
    age = models.IntegerField(null=False)

class Horses(models.Model):
    name = models.CharField(max_lenght=32, unique=True, null=False)
