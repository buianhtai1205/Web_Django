from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Customer
from .forms import CreateCustomersForm, SigninCustomersForm


def index(request):
    return render(request, 'customers/index.html', {'title':'index'})

def signin(request):
    a = SigninCustomersForm()
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

def checkCustomer(request):
    if request.method == 'POST':
        login_data = request.POST.dict()
        email = login_data['email']
        password = login_data['password']
        num_rows = Customer.objects.filter(email=email, password=password).count()
        if num_rows > 0:
            return render(request, 'customers/index.html', {'title':'index'})
        else:
            a = SigninCustomersForm
            return render(request, "customers/form_signin.html", {'form' : a})
    return HttpResponse("Sai method")


            
