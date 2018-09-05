from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from . models import Post
from django.urls import reverse_lazy

class ListBlogVista(ListView):
    model = Post
    template_name = 'home.html'

class ListBlogDetalle(DetailView):
    model = Post
    template_name = 'post_detalle.html'
    
class CrearNuevo(CreateView):
    model = Post
    template_name = "post_nuevo.html"
    fields = '__all__'

class ActualizarPost(UpdateView):
    model = Post
    fields = ['titulo', 'texto']
    template_name = 'post_edit.html'

class BorrarPost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')