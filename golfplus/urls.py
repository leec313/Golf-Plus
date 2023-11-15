# URLS.PY for all other views such as accounts etc.
from django.contrib import admin
from django.urls import path, include
from blog.views import (
    custom_404,
    custom_403,
    custom_400,
    custom_500
)
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('', include('blog.urls')),
]

# Handlers for custom error pages
handler404 = custom_404
handler403 = custom_403
handler400 = custom_400
handler500 = custom_500
