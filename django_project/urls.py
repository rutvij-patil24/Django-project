"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('blog/', include('blog.urls')), 
    # when sending this to blogs urls.py, it chops off the matched string 
    # which is '/blog' in this case. Hence it sends an empty string there 
    # and we already have an empty string matching pattern in blog urls.py

    # path('blog/about/', include('blog.urls')) this line not needed since 
    # above line sends us directly to blogs url.py,

    path('', include('blog.urls')),
    # above line will open blog home page when we just type localhost:8000
]
