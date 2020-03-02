from django import forms


class UserLoginForm(forms.Form):
#Form to log in the user
    Username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)