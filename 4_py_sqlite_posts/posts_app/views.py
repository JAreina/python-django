from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post # modelo que vamos a usar 

class Inicio(ListView):
    model = Post
    template_name = "home.html"