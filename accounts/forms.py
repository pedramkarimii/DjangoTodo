# from django.contrib.auth.models import User
# from django.forms import ModelForm

from django import forms


class UserRegisterForm(forms.Form):
    # username = forms.CharField(max_length=100)
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)