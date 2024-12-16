from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views, urls

urlpatterns = [
        path('', views.dashboard, name='dashboard'),
        path('entrar/', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
        path('sair/', auth_views.LogoutView.as_view(), {'next_page': 'registration/loged.html'}, name='logout'),
        path('cadastrar/', views.register, name='register'),
        path('nova_senha/', views.password_reset, name='password_reset'),
        path('confirmar_nova_senha/<key>', views.password_reset_confirm, name='password_reset_confirm'),
        path('editar/', views.edit, name='edit'),
        path('editar_senha/', views.edit_password, name='edit_password'),
]