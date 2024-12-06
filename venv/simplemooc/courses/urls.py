from django.urls import path
from courses.views import index, details, enrollment

app_name = 'courses'
urlpatterns = [
    path("", index, name='index'),
    #path("<int:pk>", details, name='details'),
    path("<slug>/inscricao", enrollment, name='enrollment'),    
    path("<slug>", details, name='details'),    
]