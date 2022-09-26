from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views import View
from .cart import Cart
from shop.models import Product
# Create your views here.

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(pk=id)
    quantity = request.POST["quantity"]    
    cart.add(product, quantity)
    return redirect('detail')


class CartView(View):
    template_name='cart.html'
    
    def get(self, request):
        cart = Cart(request)
    
        data = {
            "total": cart.__len__()
        }
        return render(request, self.template_name, { 'name': 'Luis Javier', 'languages': ['es', 'en'], "cart": data })