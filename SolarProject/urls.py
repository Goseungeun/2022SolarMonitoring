"""django_adminlte3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from home import views as login_view
from django.views.generic.base import TemplateView

urlpatterns=[
    url(r'^$', login_view.login.as_view(template_name='home/index.html')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='home/login.html')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/forgot-password/', TemplateView.as_view(template_name='home/forgot-password.html')),
    path('login/forgot-password-success/', TemplateView.as_view(template_name='home/forgot-password-success.html')),
    path('login/register/', TemplateView.as_view(template_name='home/register.html')),
    path('login/register-success/', TemplateView.as_view(template_name='home/register-success.html')),
    path('admin/', admin.site.urls),
]