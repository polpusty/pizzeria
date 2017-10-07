from django import forms
from django.contrib.auth import get_user_model

from .models import UserDetails

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=120)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        fields = ('email', 'first_name', 'last_name', 'email', 'password', 'username',)
        model = User


class UserDetailsForm(forms.ModelForm):
    class Meta:
        fields = ('address', 'phone',)
        model = UserDetails
