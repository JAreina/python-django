from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from . models import Post


class ListBlogVista(ListView):
    model = Post
    template_name = 'home.html'

class ListBlogDetalle(DetailView):
    model = Post
    template_name = 'post_detalle.html'
    

