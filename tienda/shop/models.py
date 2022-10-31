from pyexpat import model
from django.conf import settings
from django.db import models
from django.utils import timezone

#class User(AbstractUser):
#    pass

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'categories'
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.TextField()
    category_id = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image_file = models.ImageField(upload_to='products/images/', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "products"
        ordering = ('title', )
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self):
        return self.title


class ProductOffer(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    amount_discount = models.FloatField(default=0)
    start_date = models.DateTimeField(default=timezone.now, null=True)
    end_date = models.DateTimeField(default=timezone.now, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "products_offers"
        
    def __str__(self):
        return str(self.product_id)


class ProductLike(models.Model):
    products_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    users_id = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = "products_likes"
        unique_together = ('products_id', 'users_id',)
        
    def __str__(self):
        return str(self.products_id)
    
    
class UploadPdf(models.Model):
    grado = models.TextField(max_length=200, blank=True, null=True)
    resumes = models.FileField(upload_to="resumes/", blank=True, null=True)
    
    class Meta:
        db_table = "resumes"
        
    def __str__(self):
        return str(self.resumes)