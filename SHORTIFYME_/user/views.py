from django.shortcuts import render
from django.template import loader


# Create your views here.
def signin (request):
    return render(request, 'accounts/Login.html')