from pydoc import describe
from pyexpat import model
from statistics import mode
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


#class User(AbstractUser):
#    pass

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "categories"
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.TextField()
    category_id = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "products"
        
    def __str__(self):
        return self.title
