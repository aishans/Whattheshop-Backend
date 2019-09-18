from django.urls import path
from .views import UserCreateAPIView, ItemListView,CartListView, ModifyProductCheckoutView, DeleteProductCheckoutView,OrderHistoryView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('items/', ItemListView.as_view(), name='api-list'),
    path('cart/', CartListView.as_view(), name= "cart-list"), 
    path('product/modify/<int:product_id>/', ModifyProductCheckoutView.as_view(), name= "modify"),
    path('product/delete/<int:product_id>/', DeleteProductCheckoutView.as_view(), name= "delete"),
    path('product/history/',OrderHistoryView.as_view(),name="order-history"), 

]



urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

