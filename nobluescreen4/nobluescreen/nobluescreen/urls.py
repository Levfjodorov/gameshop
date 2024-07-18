# nobluescreen/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs
    path('', include('shop.urls')),  # Include shop URLs
]
