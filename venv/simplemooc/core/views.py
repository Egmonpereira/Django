from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admin(request):
    return render(request, 'admin/login/?next=/admin/')

def home(request):
    #return HttpResponse('Hello Word!')
    #return render(request, 'home.html', {'usuario': 'Fulano de tal'})
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')