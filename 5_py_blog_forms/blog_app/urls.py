from django.urls import path
from . import views

urlpatterns = [
path('', views.ListBlogVista.as_view(), name='home'),
path('post/<int:pk>/', views.ListBlogDetalle.as_view(), name='postdetalle'),
path('post/nuevo/', views.CrearNuevo.as_view(),name='nuevo'),
]