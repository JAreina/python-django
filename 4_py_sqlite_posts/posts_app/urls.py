# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
path('', views.Inicio.as_view(), name='home'),
]