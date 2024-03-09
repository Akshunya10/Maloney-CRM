from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import authenticate


# adduser
# class UserForm(UserCreationForm):
# 	email=forms.EmailField(max_length=50,help_text='Required. Add a valid email address')
# 	first_name=forms.CharField(max_length=50)
# 	class Meta:
# 		model=Users
# 		fields='__all__'