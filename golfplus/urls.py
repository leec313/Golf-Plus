"""golfplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog.views import (
    subscribe_newsletter,
    ProfileView,
    delete_account,
    about,
    ContactView
)
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('subscribe_newsletter/', subscribe_newsletter,
         name='subscribe_newsletter'),
    path('profile/', ProfileView, name='profile'),
    path('delete_account/', delete_account, name='delete_account'),
    path("accounts/", include("allauth.urls")),
    path("about/", about, name='about'),
    path("contact/", ContactView, name='contact'),
    path('', include('blog.urls')),
]
