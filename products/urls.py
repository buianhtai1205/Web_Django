from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('1/', views.myFirstChart , name="demo"),
   path('2/', views.myFirstChart2 , name="demo"),
]
