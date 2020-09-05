from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import curdmodels


class curdForm(forms.ModelForm):
    class Meta:
        model = curdmodels
        fields = ["title", "description", "img"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
