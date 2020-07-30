from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.home),
   path('update/<str:pk>/', views.updateEvent, name= "update_event"),
   path('delete/<str:pk>/', views.deleteEvent, name= "delete_event"),
   path('register', views.registerUser, name="register")

]
