from django.contrib import admin

from .models import Category, Product, ProductLike, ProductOffer

# Register your models here.
# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active', 'category_id')
    list_filter = ('is_active', 'category_id', 'created_at', 'updated_at')
    list_editable = ['is_active']
    
admin.site.register(Product)
admin.site.register(ProductOffer)
admin.site.register(ProductLike)