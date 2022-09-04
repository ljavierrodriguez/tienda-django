from pydoc import describe
from statistics import mode
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


#class User(AbstractUser):
#    pass

class Category(models.Model):
    __tablename__ = "categories"
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
