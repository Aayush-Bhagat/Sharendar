from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('events',views.events, name="events"),
   path('update/<str:pk>/', views.updateEvent, name= "update_event"),
   path('delete/<str:pk>/', views.deleteEvent, name= "delete_event"),
   path('register', views.registerUser, name="register"),
   path('login', views.loginUser, name="login"),
   path('logout', views.logoutUser, name="logout"),


]
