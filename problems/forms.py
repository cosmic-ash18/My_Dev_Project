from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# UserCreationFor by default only has username, password1 and password2
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
