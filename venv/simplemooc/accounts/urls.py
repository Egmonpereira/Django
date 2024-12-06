from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

app_name = 'accounts'
urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("entrar/", LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #path('sair/', LoginView.as_view(next_page='#'), name='logout'),
    path("sair/", logout_then_login, {'login_url':'core:home'}, name='logout'),
    path("cadastrar/", views.register, name='register'),
    path("nova-senha/", views.password_reset, name='password_reset'),
    path("Confirmar-nova-senha/(<key>)", views.password_reset_confirm, name='password_reset_confirm'),
    path("editar/", views.edit, name='edit'),
    path("editar-senha/", views.edit_password, name='edit_password'),
]