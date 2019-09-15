from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import UserCreateSerializer, ItemListSerialzer
from .models import ProductDetail

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListView(ListAPIView):
	queryset = ProductDetail.objects.all()
	serializer_class = ItemListSerialzer
	filter_backends = [SearchFilter, OrderingFilter,]
	search_fields = ['name'] 
