from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


app_name = 'backend'
urlpatterns = [
   path(r'',views.home, name="home"),
   url(r'eventslist',views.events, name="events"),
   path(r'update/<str:pk>/', views.updateEvent, name= "update_event"),
   path(r'delete/<str:pk>/', views.deleteEvent, name= "delete_event"),
   url(r'register', views.registerUser, name="register"),
   url(r'login/', views.loginUser, name="login"),
   url(r'logout', views.logoutUser, name="logout"),
   url(r'^calendar/$', login_required(views.CalendarView.as_view()), name='calendar'),
]
