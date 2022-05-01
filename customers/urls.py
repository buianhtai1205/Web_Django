from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('save/', views.saveCustomer, name='save'),
    path('check/', views.checkCustomer, name='check'),
]