from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.home, name=''),
    path('index/', views.home, name='inicio'),
    path('contat/', views.contact, name='contato'),
    path('admin/', views.adminin, name='admin'),
]