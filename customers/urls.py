from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('save/', views.saveCustomer, name='save'),
    path('check/', views.checkCustomer, name='check'),
]