from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import LoginForm
from django.conf import settings
from django.contrib.auth import authenticate, login as django_login
# Create your views here.
class Login(View):
    template_name = 'registration/login.html'
    def get(self, request): 
        if request.user.is_authenticated:
            return redirect('home')  
        form = LoginForm()
        return render(request, self.template_name, { 'form': form })
    
    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username, password = form.cleaned_data['username'], form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('home')
            else:
                form.add_error("password", "Username/Password are incorrects")
                return render(request, self.template_name, {'form': form })
        return render(request, self.template_name, { 'form': form })