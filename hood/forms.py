from django import forms
from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name','admin','email','hood_id','user']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'user', 'hood','post_id']

