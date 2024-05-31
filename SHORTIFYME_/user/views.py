
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def register_us(request):
    return render(request, 'accounts/Register.html')

def login_us(request):
    return render(request, 'accounts/Login.html')