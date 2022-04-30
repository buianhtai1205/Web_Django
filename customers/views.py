from django.shortcuts import render

# Create your views here.
from .models import Customer
from .forms import CreateCustomersForm

def index(request):
    return render(request, 'customers/index.html', {'title':'index'})

def signin(request):
    a = CreateCustomersForm()
    return render(request, "customers/form_signin.html", {'form' : a})

def signup(request):
    a = CreateCustomersForm()
    return render(request, "customers/form_signup.html", {'form' : a})

def saveCustomer(request):
    if request.method == 'POST':
        a = CreateCustomersForm(request.POST)
        if a.is_valid():
            a.save()
            return render(request, 'customers/index.html', {'title':'index'})
            
