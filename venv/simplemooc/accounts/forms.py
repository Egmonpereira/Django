from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from core.utils import generate_hash_key
from core.mail import send_mail_templates
from .models import PasswordReset

User = get_user_model()

class PasswordResetForm(forms.Form):
    
    email = forms.EmailField(label="E-mail")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            'Email de usuário não encontrado!'
        )

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'registration/password_reset_mail.html'
        subject ='Criar nova senha!'
        context = {
            'reset': reset,
        }
        send_mail_templates(subject, template_name, context, [user.email])

class RegisterForm(forms.ModelForm):

    #email = forms.EmailField(label='E-mail')
    
    #O que está comentado não faz mais sentido, pois no nosso models eles já fazem esta verificação
    #def clean_email(self):
    #    email = self.cleaned_data['email']
    #    if User.objects.filter(email=email).exists():
    #        raise forms.ValidationError('E-mail já cadastrado!')
    #    return email

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    def clean_old_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'As senhas não conferem',
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        #user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    class Meta:
        model = User
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):

    #def clean_email(self):
    #    email = self.cleaned_data['email']
    #    if User.objects.filter(email=email).exclude(pk=self.instance.pk):
    #        if queryset.exists():
    #            raise forms.ValidationError('E-mail já cadastrado!')
    #    return email
    
    class Meta:
        model = User
    #    fields = ['username', 'email', 'first_name', 'last_name']
        fields = ['username', 'email', 'name']