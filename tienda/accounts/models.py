from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True, blank=False, null=False)
    rut = models.CharField(max_length=200, unique=True, blank=False, null=False)
    phone = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        ordering = ('rut',)
        verbose_name = 'user'
        verbose_name_plural = 'users'