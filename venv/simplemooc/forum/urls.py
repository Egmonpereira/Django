from django.contrib import admin
from django.urls import path, include
from forum import views, urls

urlpatterns = [
        path('', views.index, name='index'),
]