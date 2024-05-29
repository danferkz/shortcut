
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'accounts/Register.html')

def reg(request):
    return render(request, 'accounts/Register.html')