from django.urls import path
from . import views 

urlpatterns = [
    path('cart/<int:id>/add', views.cart_add, name="add"),
    path('cart/', views.CartView.as_view(), name="detail")
]
