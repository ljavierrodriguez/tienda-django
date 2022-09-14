from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static

from . import views 

urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html'), name="home"),
    #path('blog/', TemplateView.as_view(template_name='blog.html'), name="blog"),
    #path('', views.home, name="home"),
    #path('blog/', views.blog, name="blog")
    path('', views.HomeView.as_view(), name="home"),
    path('blog/', views.BlogView.as_view(), name="blog"),
    path('products/', views.ProductsView.as_view(), name="products")
]
