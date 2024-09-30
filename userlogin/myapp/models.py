from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    value=models.CharField(max_length=100)