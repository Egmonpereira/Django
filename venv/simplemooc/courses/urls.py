from django.contrib import admin
from django.urls import path, include
from courses import views, urls

urlpatterns = [
        path('', views.index, name='index'),
        #path('<int:pk>/', views.details, name='details'),
        path('course/<slug>/', views.details, name='details'),
        path('inscricao/<slug>/', views.enrollment, name='enrollment'),
        path('anuncios/<slug>/', views.announcements, name='announcement'),
        path('cancelar/<slug>/', views.undo_enrollment, name='undo_enrollment'),
        path('anuncios/<slug>/<pk>/', views.show_announcement, name='show_announcement'),
        path('aulas/<slug>/', views.lessons, name='lessons'),
        path('aula/<slug>/<pk>', views.lesson, name='lesson'),
        path('materiais/<slug>/<pk>', views.material, name='material'),
]