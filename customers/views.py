from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Customer
from products.models import Product
from .forms import CreateCustomersForm, SigninCustomersForm
from django.urls import reverse
from django.http import JsonResponse
from django.core.serializers import serialize


def index(request):
    content = {}
    if request.session._session:
        if (request.session['username']):
            username = request.session['username']
            content['username'] = username
    products_iphone = Product.objects.filter(manufacturer_id = 15)
    content['ds_product_iphone'] = products_iphone
    return render(request, 'customers/index.html', content)

def signin(request):
    a = SigninCustomersForm()
    return render(request, "customers/form_signin.html", {'form' : a})

def signout(request):
    del request.session['username']
    return redirect(reverse('customers:index', kwargs = {}))

def signup(request):
    a = CreateCustomersForm()
    return render(request, "customers/form_signup.html", {'form' : a})

def saveCustomer(request):
    if request.method == 'POST':
        a = CreateCustomersForm(request.POST)
        if a.is_valid():
            email = request.POST.dict()['email']
            username = email.split('@')[0]
            request.session['username'] = username
            a.save()
            return redirect(reverse('customers:index', kwargs = {}))

def checkCustomer(request):
    if request.method == 'POST':
        login_data = request.POST.dict()
        email = login_data['email']
        password = login_data['password']
        num_rows = Customer.objects.filter(email=email, password=password).count()
        if num_rows > 0:
            username = email.split('@')[0]
            request.session['username'] = username
            messages = "Đăng nhập thành công!"
            content = {'username': username, 'messages': messages}
            return redirect(reverse('customers:index', kwargs = {}))
        else:
            messages = "Email hoặc mật khẩu không đúng!"
            content = {'messages': messages}
            return redirect('customers:signin')
    return HttpResponse("Sai method")


            
