from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class Registerform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ["username", "email","password1", "password2",]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    SEX_CHOICES = (('F', 'Female',),('M', 'Male',),('U', 'Unsure',),)
    sex = forms.ChoiceField(choices=SEX_CHOICES,)

    class Meta:
        model = User 
        fields = ["username", "email","first_name","last_name","sex" ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']