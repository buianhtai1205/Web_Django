from django.urls import path
from . import views
app_name = 'carts'

urlpatterns = [
    path('', views.cart_details, name="cart_details"),
    path('add', views.add_to_cart, name="add_to_cart"),
    path('remove/<int:id>', views.remove_from_cart, name="remove"),
    path('clear/', views.clear_cart, name="clear"),
    path('check-out',views.CheckOut, name='check-out'),
]