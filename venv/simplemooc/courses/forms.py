from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_templates

from .models import Comment

class ContactCourse(forms.Form):
    
    name = forms.CharField(label='Nome', max_length=100)
    email =forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Dúvidas', widget=forms.Textarea
    )

    def send_mail(self, course):
        subject = '[%s] Contato' % course
        #message = 'Nome: %(name)s;E-mail: %(email)s;Mensagem: %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        #message = message % context
        #send_mail(
        #    subject, message, settings.DEFAULT_FROM_EMAIL,
        #    [settings.CONTACT_EMAIL]
        #)
        template_name = 'courses/contact_email.html'
        send_mail_templates(
            subject, 
            template_name, 
            context,
            [settings.CONTACT_EMAIL]
        )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']    