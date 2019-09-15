from django.urls import path
from .views import UserCreateAPIView, ItemListView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('api/items', ItemListView.as_view(), name='api-list'),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

