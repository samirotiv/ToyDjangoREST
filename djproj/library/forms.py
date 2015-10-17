# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:09:37 2015

@author: HP-PC
"""
from django import forms
from django.forms import ModelForm,PasswordInput
from .models import LibraryUser
class LoginForm(forms.Form):
    user_name = forms.CharField(label="User Name:",max_length=100)
    passwd = forms.CharField(label=
    "Password:",max_length=32,widget=forms.PasswordInput)
    
class LibraryUserForm(ModelForm):
    class Meta:
        model = LibraryUser
        fields = ['username','password','usertype']
        widgets = {
            'password': PasswordInput(),
        }

class RegisterForm(forms.Form):
    USER_TYPE_CHOICES = (
        ('C', 'Customer'),
        ('L', 'Librarian'),
    )    
    user_name = forms.CharField(label="User Name:",max_length=100)
    passwd = forms.CharField(label="Password:",max_length=32,
                             widget=forms.PasswordInput)
    usertype = forms.ChoiceField(choices=USER_TYPE_CHOICES)
    
class OrderForm(forms.Form):
    TITLE = 'title'
    AUTHOR = 'author'
    PUBLISHER = 'publisher'
    COUNT = 'count'
    DATE_ADDED = 'date_added'    
    ORDERING_CHOICES = (
        (TITLE,'Title'),
        (AUTHOR,'Author'),
        (PUBLISHER,'Publisher'),
        (COUNT,'Count'),
        (DATE_ADDED,'Date Added'),    
    )
    order = forms.ChoiceField(choices=ORDERING_CHOICES)

class RequestForm(forms.Form):
    title = forms.CharField(label="Enter the title:",max_length=100)
    copies_required = forms.IntegerField() 

