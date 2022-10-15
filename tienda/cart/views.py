from django.shortcuts import get_object_or_404, render, redirect
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

@require_POST
def cart_remove(request, id):
    cart = Cart(request)
    product = Product.objects.get(pk=id)
    cart.remove(product)
    return redirect('detail')

@require_POST
def cart_update(request, id):
    cart = Cart(request)
    product = Product.objects.get(pk=id)
    quantity = request.POST["quantity"]
    override = request.POST["override_quantity"]    
    override_quantity = True if override else False
    cart.add(product, quantity, override_quantity)
    return redirect('detail')


class CartView(View):
    template_name='cart.html'
    
    def get(self, request):
        cart = Cart(request)
        total = cart.__len__()
        return render(request, self.template_name, { "cart": cart, "total": total })