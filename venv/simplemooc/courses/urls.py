from django.contrib import admin
from django.urls import path, include
from courses import views, urls

urlpatterns = [
        path('', views.index, name='index'),
        #path('<int:pk>/', views.details, name='details'),
        path('cursos/<slug:slug>/', views.details, name='details')
]