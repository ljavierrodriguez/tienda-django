from django.shortcuts import redirect, render
from django.views import View
from .models import Product, UploadPdf
from cart.cart import Cart
'''
def home(request):
    template_name = "index.html"
    
    return render(request, template_name, { 'name': 'Luis'})


def blog(request):
    template_name = "blog.html"
    
    return render(request, template_name, {})

'''

class HomeView(View):
    template_name='index.html'
    
    def get(self, request):
        cart = Cart(request)
    
        total = cart.__len__()
        return render(request, self.template_name, { 'name': 'Luis Javier', 'languages': ['es', 'en'], "total": total })
    
    # Esta funcion se utiliza si recibo datos por un formulario
    def post(self, request):
        return render(request, self.template_name, {})
    
    
class BlogView(View):
    template_name='blog.html'
    
    def get(self, request):
        cart = Cart(request)
    
        total = cart.__len__()
        return render(request, self.template_name, { 'name': 'Luis Javier', "total": total })
    
    # Esta funcion se utiliza si recibo datos por un formulario
    def post(self, request):
        return render(request, self.template_name, {})
    
    
class ProductsView(View):
    template_name='products.html'
    
    def get(self, request):
        products = Product.objects.all().select_related('category_id')
        cart = Cart(request)
    
        total = cart.__len__()
        
        print(products)
        return render(request, self.template_name, {"products": products, "total": total })
    
class ProductDetailsView(View):
    template_name='product_details.html'
    
    def get(self, request, id = None):
        cart = Cart(request)
        total = cart.__len__()
        product = Product.objects.get(pk=id)
        return render(request, self.template_name, {"product": product, "total": total })
    

class UploadFilesView(View):
    template_name='upload.html'
    
    def get(self, request):
        cart = Cart(request)
        total = cart.__len__()
        
        files = UploadPdf.objects.all()
        
        return render(request, self.template_name, {"total": total, "files": files })
    
    def post(self, request):
        
        #print(request.POST)
        #print(request.FILES)
        files = request.FILES.getlist('file')
        for file in files:
            file_instance = UploadPdf(resumes=file)
            file_instance.save()
        
        return redirect('/upload-files/')
    
class DeleteUploadFiles(View):
    def get(self, request, id):
        
        file = UploadPdf.objects.get(pk=id)
        
        file.delete()
        
        return redirect('/upload-files/')