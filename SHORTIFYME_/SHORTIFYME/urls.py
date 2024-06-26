"""
URL configuration for SHORTIFYME project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static 
from django.conf import settings
from django.urls import path, include  # Mantén solo una importación de path y include
from base import views as base_views  # Importa views de base con un alias para evitar confusión
#from user import views as user_views  # Importa views de user con un alias

urlpatterns = [
    path('home/', base_views.home, name='home'),  # Asegúrate de agregar una barra diagonal al final
    path('', base_views.base, name='base'),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('card/', include('cards.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#handler404 = 'user.views.error_404'
