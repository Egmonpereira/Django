from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.home, name=''),
    path('index/', views.home, name='inicio'),
    path('contato/', views.contact, name='contato'),
    path('admin/', views.admin, name='admin'),
]