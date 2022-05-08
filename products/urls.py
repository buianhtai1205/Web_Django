from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('1/', views.myFirstChart , name="firstChart"),
   path('2/', views.mySecondChart , name="secondChart"),
]
