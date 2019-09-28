from django.urls import path
from .views import UserCreateAPIView, ProfileView, ItemListView,CartListView, CartChangeView,ModifyProductCheckoutView,ProductDetailView, ProductCheckoutView,DeleteProductCheckoutView,OrderHistoryView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('items/', ItemListView.as_view(), name='api-list'),
    path('cart/', CartListView.as_view(), name= "cart-list"), 
    path('product/detail/', ProductDetailView.as_view(), name= "detail-list"),
    path('product/add/', ProductCheckoutView.as_view(), name = "add-to-cart"),
    path('product/modify/<int:product_id>/', ModifyProductCheckoutView.as_view(), name= "modify"),
    path('product/delete/<int:product_id>/', DeleteProductCheckoutView.as_view(), name= "delete"),
    path('cart/checkout/', CartChangeView.as_view(), name="cart-checkout"),
    path('user/history/',OrderHistoryView.as_view(),name="order-history"), 
    path('profile/', ProfileView.as_view(),name="profile"), 

]

#checkout #orderHistory

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

