from django.shortcuts import render

# Create your views here.
from .models import Customer

def signin(request):
    return render(request, "customers/form_signin.html")

def signup(request):
    return render(request, "customers/form_signup.html")