from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # calls home function in views.py
    path('about/', views.about, name='blog-about'), # calls about function in views.py
]