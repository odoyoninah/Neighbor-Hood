import email
from multiprocessing import context
from django.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from hood.models import Post
from .forms import *
from django.contrib.auth.decorators import login_required
#handle all the status code responses.

def index(request):
    post = Post.objects.all()
    return render(request,'index.html')

def business(request):
    return render(request,'business.html')

@login_required(login_url='/accounts/login/')
def createpost(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('index')
    else:
        form = PostForm()
    return render(request,'createpost.html',{'form':form}) 

@login_required(login_url='/accounts/login/')
def createbusiness(request):
    if request.method=='POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('business')
    else:
        form = BusinessForm()
    return render(request,'createbusiness.html',{'form':form}) 






def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
        
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})


    
def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('index')

