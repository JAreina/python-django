# pages/urls.py
from django.urls import path
from . import views
urlpatterns = [
 path('', views.Inicio.as_view(), name='inicio'),
 path('sobremi/',views.SobreMi.as_view(), name='SOBRE MI')
]