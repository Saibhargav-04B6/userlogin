from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Product

@receiver(post_save)
def create_product(created,**kwargs):
    if created:
        Product.objects.create(name="Brinjal",type="Vegetable",value="2")