from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    path('createcard/', views.createcard, name= 'createcard'),
    
    ]