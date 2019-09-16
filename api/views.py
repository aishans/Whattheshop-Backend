from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import *
from .models import *

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListView(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ItemListSerialzer
	filter_backends = [SearchFilter, OrderingFilter,]
	search_fields = ['name'] 

class ProductCheckoutView(CreateAPIView):
	serializer_class = ProductCheckoutSerializer

class ModifyProductCheckoutView(RetrieveUpdateAPIView):
	queryset = ProductCheckout.objects.all()
	serializer_class = ModifyProductCheckoutSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'

class CartListView(ListAPIView):
	queryset = ProductCheckout.objects.all()
	serializer_class = ProductCheckoutSerializer

class CartView(CreateAPIView):
	serializer_class = CartSerializer

# class ModifyCartView(RetrieveUpdateAPIView):
# 	serializer_class = CartSerializer

class DeleteProductCheckoutView(DestroyAPIView):
	queryset = ProductCheckout.objects.all()
	serializer_class = ModifyProductCheckoutSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'

