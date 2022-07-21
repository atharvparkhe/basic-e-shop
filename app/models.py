from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from base.models import *
from .threads import send_contact_email
from .validators import *


class ContactUsModel(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    def __str__(self):
        return self.name


class CategoryModel(BaseModel):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="category", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name


class ProductModel(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, related_name="product_category", on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.FloatField()
    img = models.ImageField(upload_to="product", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name

@receiver(pre_save, sender=ContactUsModel)
def send_email(sender, instance, *args, **kwargs):
    thread_obj = send_contact_email(instance.email)
    thread_obj.start()