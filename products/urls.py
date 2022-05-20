from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('1/', views.myFirstChart , name="firstChart"),
   path('2/', views.mySecondChart , name="secondChart"),
   path('3/', views.myThirdChart , name="thirdChart"),
   path('4/', views.myFourthChart , name="fourthChart"),
   path('5/', views.myFifthChart , name="fifthChart"),
]
