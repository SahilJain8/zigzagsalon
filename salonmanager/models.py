from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class Service(models.Model):
    category = models.CharField(max_length=100,default='Hair Services')
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')
    image = models.ImageField(upload_to='product_images/', null=True)
    duration = models.DurationField()

    def __str__(self):
        return self.name
class Manager(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')
    image = models.ImageField(upload_to='product_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


