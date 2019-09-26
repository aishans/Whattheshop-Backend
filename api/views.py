from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemListSerialzer
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['name'] 

class ProductCheckoutView(CreateAPIView):
    serializer_class = ProductCheckoutSerializer
   
    def perform_create(self, serializer):
        serializer.save(cart=Cart.objects.get(user=self.request.user, cart_in_use=True))

class ModifyProductCheckoutView(RetrieveUpdateAPIView):
    queryset = ProductCheckout.objects.all()
    serializer_class = ModifyProductCheckoutSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProductDetailView(ListAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

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

class CartChangeView(APIView):
    def get(self, request):
        cart_current = Cart.objects.get(user=request.user, cart_in_use=True)
        cart_current.cart_in_use = False
        cart_current.save()
        new_cart = Cart.objects.create(user=request.user, cart_in_use=True)
        return Response({"status": "ok"})
        
        
            

class OrderHistoryView(ListAPIView):
    serializer_class = CartDetailSerializer
    # queryset = Cart.objects.filter(user=request.user, cart_in_use=False)
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, cart_in_use=False)
