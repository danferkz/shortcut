from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/Home.html')

def base(request):
    return render(request, 'Base.html')