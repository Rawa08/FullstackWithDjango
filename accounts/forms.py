from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
#Form to log in the user
    Username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
#Form to register the user
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')   
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'This Email address is alredy registered') 
        return email   

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')  
        password2 = self.cleaned_data.get('password2') 

        if not password1 or not password2:
            raise ValidationError('please confirm your password')

        if password1 != password2:
            raise ValidationError('Password 1 and Password 2 must match')  

        return password2      
