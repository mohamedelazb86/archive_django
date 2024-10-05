from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ActivateForm(forms.Form):
    code=forms.CharField(max_length=75)