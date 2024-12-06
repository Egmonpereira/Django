from django.urls import path, re_path
from core.views import home, contact

app_name = 'core'
urlpatterns = [
    path("", home, name='home'),
    re_path(r'^contact.html/$', contact, name='contact'),
]