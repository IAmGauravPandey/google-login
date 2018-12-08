from django.shortcuts import render,get_object_or_404,redirect
from django.http import *
from django.contrib import admin,auth


# Create your views here.

def home(request):
	return render(request, 'myapp/home.html')

def login(request):
    return render(request,'myapp/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'myapp/home.html')