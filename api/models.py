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


    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_in_use= models.BooleanField(default=True)


class ProductCheckout(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="product_checkouts")
   
   
# class User(models.Model):
# 	username = models.CharField(max_length=120)
# 	civil_ID = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    # products = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

