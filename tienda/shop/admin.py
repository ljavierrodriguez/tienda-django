from django.contrib import admin

from .models import Category, Product, ProductLike, ProductOffer

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOffer)
admin.site.register(ProductLike)