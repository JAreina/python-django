from django.urls import path
from . import views

urlpatterns = [
path('', views.ListBlogVista.as_view(), name='home'),
path('post/<int:pk>/', views.ListBlogDetalle.as_view(), name='postdetalle'),
path('post/nuevo/', views.CrearNuevo.as_view(),name='postnuevo'),
path('post/<int:pk>/edit/',views.ActualizarPost.as_view(), name='postedit'),
path('post/<int:pk>/delete/',views.BorrarPost.as_view(), name='postdelete'),
]