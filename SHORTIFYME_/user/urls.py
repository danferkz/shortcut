from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
   path('register/', views.register_us, name='register'),  # Asegúrate de agregar una barra diagonal al final
   path('login/', views.login_us, name='login'),  # Cambia 'login_' a 'login' y agrega una barra diagonal al final
]