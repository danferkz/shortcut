from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
   path('register', views.register_us, name='register'),
   path('login', views.login_us, name='login'),
]