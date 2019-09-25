from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class ProfileSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model= Profile
        fields=['name',]


class ItemListSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= ['name', 'image', 'price']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','image', 'price']
class ProductCheckoutSerializer(serializers.ModelSerializer):
    product = ProductSerializer1()
    class Meta:
        model= ProductCheckout
        fields= ['product','quantity', 'price']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class ModifyProductCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCheckout
        fields= ['quantity']