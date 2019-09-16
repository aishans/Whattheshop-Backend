from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated]
    
class ItemListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemListSerialzer
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['name'] 
    permission_classes = [IsAuthenticated]

class ProductCheckoutView(CreateAPIView):
    serializer_class = ProductCheckoutSerializer
    permission_classes = [IsAuthenticated]

class ModifyProductCheckoutView(RetrieveUpdateAPIView):
    queryset = ProductCheckout.objects.all()
    serializer_class = ModifyProductCheckoutSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
    permission_classes = [IsAuthenticated]

class CartListView(ListAPIView):
    queryset = ProductCheckout.objects.all()
    serializer_class = ProductCheckoutSerializer
    permission_classes = [IsAuthenticated]

class CartView(CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# class ModifyCartView(RetrieveUpdateAPIView):
# 	serializer_class = CartSerializer

class DeleteProductCheckoutView(DestroyAPIView):
    queryset = ProductCheckout.objects.all()
    serializer_class = ModifyProductCheckoutSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
    permission_classes = [IsAuthenticated, IsAdminUser]
