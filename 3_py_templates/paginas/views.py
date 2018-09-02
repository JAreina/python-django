from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Inicio(TemplateView):
   template_name = 'home.html'



#   http://127.0.0.1:8000/sobremi/
class SobreMi(TemplateView):
    template_name = 'sobremi.html'
