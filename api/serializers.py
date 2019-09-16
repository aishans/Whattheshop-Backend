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
    past_orders= serializers.SerializerMethodField()
    
    class Meta:
        model= Profile
        fields=['name','products']
    def get_past_orders(self,obj):
        user_obj = obj.user
        order_list= user.orders.all()
        order_list = ProductCheckout.objects.filter(user=user_obj)
        return ProductSerializer(order_list, many=True).data



class ItemListSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= ['name', 'image']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','image']
class ProductCheckoutSerializer(serializers.ModelSerializer):
    product = ProductSerializer1()
    class Meta:
        model= ProductCheckout
        fields= ['product','quantity']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class ModifyProductCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCheckout
        fields= ['quantity']