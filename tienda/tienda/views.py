from django.shortcuts import render
from django.views import View

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
        return render(request, self.template_name, { 'name': 'Luis Javier'})
    
    # Esta funcion se utiliza si recibo datos por un formulario
    def post(self, request):
        return render(request, self.template_name, {})
    
    
class BlogView(View):
    template_name='blog.html'
    
    def get(self, request):
        return render(request, self.template_name, { 'name': 'Luis Javier'})
    
    # Esta funcion se utiliza si recibo datos por un formulario
    def post(self, request):
        return render(request, self.template_name, {})
