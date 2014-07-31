from django.db import models

# Create your models here.

class OwnerModel(models.Model):
    owner = models.ForeignKey(User)

class Engine(models.Model):
    name = models.TextField()
