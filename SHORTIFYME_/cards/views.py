from django.shortcuts import render
"""
from .forms import CardForm

"""
# Create your views here.
def createcard(request):
    return render(request, 'home/createcard.html') 