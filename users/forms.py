from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name','password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfieUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']
