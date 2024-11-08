from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    catogary = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10)
    total = models.FloatField()