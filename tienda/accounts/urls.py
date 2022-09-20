from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name="custom.login"),
    path('', include('django.contrib.auth.urls')),
]