from django.urls import path
from .views import UserCreateAPIView, ItemListView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('api/items', ItemListView.as_view(), name='api-list'),
]