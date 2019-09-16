from django.contrib import admin
from .models import Product,ProductCheckout,Cart

admin.site.register(Product)
admin.site.register(ProductCheckout)
admin.site.register(Cart)
