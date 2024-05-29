
from django.shortcuts import render
from django.http import HttpResponse

def register_us(request):
    return render(request, 'accounts/Register.html')

def login_us(request):
    return render(request, 'account/Login.html')