# URLS.PY for all other views suc as newsletter, accounts, contact page etc.
from django.contrib import admin
from django.urls import path, include
from blog.views import (
    subscribe_newsletter,
    ProfileView,
    delete_account,
    about,
    ContactView,
    custom_404
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

handler404 = custom_404
