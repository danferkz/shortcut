from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('home/', views.home, name='home'),
    
]