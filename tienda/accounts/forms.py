from django import forms
from django.forms import Form
from .models import User

class LoginForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'password']