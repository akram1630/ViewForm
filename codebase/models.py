from os import name
from django.db import models

# Create your models here.

class CRUD(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  level = models.CharField(max_length=30)
  date = models.DateField(auto_now_add=True)
  def __Str__(self):
    return self.name
