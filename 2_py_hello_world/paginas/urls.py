from django.urls import path

from . import views

urlpatterns = [
    path('',views.verPagina,name="INICIO")
]