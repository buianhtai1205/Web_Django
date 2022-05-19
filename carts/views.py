from django.shortcuts import render

# Create your views here.
from ast import arg
from django.shortcuts import render, get_object_or_404, redirect
from numpy import product
from requests import session
from carts.cart import Cart
import customers
from customers.models import Customer, Order, OrderProduct
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from carts.forms import CartAddProductForm
from manufacturers.models import Manufacturer
# Create your views here.


@login_required
@require_POST
def add_to_cart(request):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        product_id = form.cleaned_data['product_id']
        quantity = form.cleaned_data['quantity']
        product = get_object_or_404(Product, id=product_id)
        cart.add(product_id, product.price, quantity)
        messages.success(request, f'{product.name} added to cart.')
    return redirect('carts:cart_details')


@login_required
def cart_details(request):
    cart = Cart(request)
    products = Product.objects.filter(pk__in=cart.cart.keys())
    manufacturers = Manufacturer.objects.all()
    def map_function(p):
        pid = str(p.id)
        q = cart.cart[pid]['quantity']
        return {'product': p, 'quantity': q, 'total': p.price*q, 'form': CartAddProductForm(initial={'quantity': q, 'product_id': pid})}
    cart_items = map(map_function, products)
    return render(request, 'carts/cart_detail.html', {'cart_items': cart_items, 'total':cart.get_total_price, 'manufacturers': manufacturers})


@login_required
def remove_from_cart(request, id):
    cart = Cart(request)
    cart.remove(str(id))
    return redirect('carts:cart_details')


@login_required
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('carts:cart_details')

def CheckOut(request):
    email = ''
    if 'username' in request.session:
        if (request.session['username']):
            username = request.session['username']
            email = username + '@gmail.com'
    customer = Customer.objects.filter(email=email)[0]
    cart = Cart(request)
    total_prices = cart.get_total_price()
    order = Order(  name_receiver = customer.name,               
                    phone_receiver = customer.phone,
                    address_receiver = customer.address,
                    messages = 'giao sớm',
                    total_price = total_prices,
                    customer_id_id = customer.id
            )
    order.PlaceOrder()
    orders = Order.objects.filter(name_receiver = customer.name)[0]
    quantity_id = None
    
    products = Product.objects.filter(pk__in=cart.cart.keys())
    for product in products:
        quantity_id = cart.cart[str(product.id)]['quantity']
        order_product = OrderProduct(order_id = orders.id,
                        product_name = product.name,
                        quantity = quantity_id

        )
        order_product.save()
    cart.clear()
    return redirect('carts:cart_details')