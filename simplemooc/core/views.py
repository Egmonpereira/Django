#VIEWS: o que o usuário vai ver, quais dados serão visualizados

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
 