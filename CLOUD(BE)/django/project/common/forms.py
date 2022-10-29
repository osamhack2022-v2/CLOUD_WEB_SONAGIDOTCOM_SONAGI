from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    enlist_day = forms.DateField(label="입대일")
    discharge_day = forms.DateField(label="전역일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "enlist_day", "discharge_day")     