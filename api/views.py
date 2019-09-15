from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import UserCreateSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListView(ListAPIView):
	queryset = ProductDetail.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [SearchFilter, OrderingFilter,]
	search_fields = ['name'] 
