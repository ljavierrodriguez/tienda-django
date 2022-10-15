from django.urls import path
from . import views 

urlpatterns = [
    path('cart/<int:id>/add', views.cart_add, name="add"),
    path('cart/<int:id>/remove', views.cart_remove, name="remove"),
    path('cart/<int:id>/update', views.cart_update, name="update"),
    path('cart/', views.CartView.as_view(), name="detail")
]
