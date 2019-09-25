from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=120)
    skin_color = models.CharField(max_length=120)
    blood_type = models.CharField(max_length=120)
    amputation_date = models.DateTimeField(auto_now_add=True)
    expiary_date = models.DateTimeField(auto_now_add=True)
    reason_for_amputation = models.TextField()
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=3)

class ProductCheckout(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   
# class User(models.Model):
# 	username = models.CharField(max_length=120)
# 	civil_ID = models.IntegerField()

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

