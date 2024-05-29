from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    #registration
    path('register/', views.register, name='register'),
]