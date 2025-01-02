"""
URL configuration for projeto_lumava project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from app_gerenciamento import views as app_views
from app_user import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home'),
    path('login/', user_views.user_login, name='login'),
    path('registro/', user_views.user_register, name='register'),
    path('logout/', user_views.user_logout, name='user_logout'),
    path('servico/', app_views.servico, name='servico'),
    path('registrar_os/', app_views.registrar_os, name='registrar_os'),
    path('info_os/<slug:slug>/', app_views.info_os, name='info_os')
] 
